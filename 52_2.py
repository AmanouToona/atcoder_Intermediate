# JOI 2017 予選 4 - ぬいぐるみの整理

# 貰うDP
# DPテーブルには取り出さないでよいぬいぐるみの個数を保存する
# こちらの実装はメモリが足りない

import sys


def main():
    # 入力 --------------------------------------
    N, M = map(int, sys.stdin.readline().strip().split())

    # 累積和をとっておいて、抜き出さずに済むぬいぐるみの個数を高速に計算する
    sum_table = [[0] * (N + 1) for _ in range(M)]

    for n in range(N):
        type = int(sys.stdin.readline().strip())
        sum_table[type - 1][n + 1] = 1

        for m in range(M):
            sum_table[m][n + 1] += sum_table[m][n]

    # dp 準備 --------------------------------------
    dp = [[None] * 2 for _ in range(2 ** M)]

    # dp 更新関数
    def dfs(v):
        # v: 考慮したぬいぐるみの種類の bit

        if dp[v][0] is not None:
            return dp[v]

        # 終端条件
        if v == 0:
            return [0, None]

        ans = 0
        for u in range(M):  # 今追加したぬいぐるみの種類をu とする
            if (v >> u) & 1 == 1:  # 種類u のぬいぐるみが考慮したぬいぐるみの 集合v に入っている

                # 取り出さなくてよいぬいぐるみの個数を計算する ---------
                # 今までに計算してあるぬいぐるみの個数を計算する
                right = dp[v][1]
                left = right - sum_table[u][-1]
                dp[v ^ (1 << u)][1] = left

                # 取り出さなくてよいぬいぐるみの個数は?
                no_draw = sum_table[u][right] - sum_table[u][left]

                # print(f'right: {right}, left: {left}, no_draw: {no_draw}, '
                #       f'u: {format(u, "b")}, v: {format(v, "b")}, no_draw: {no_draw}')
                # print(f'dfs: {v ^ (1 << u)}')
                ans = max(ans, dfs(v ^ (1 << u))[0] + no_draw)

        dp[v][0] = int(ans)
        return dp[v]

    dp[2 ** M - 1][1] = N
    ans = dfs(2 ** M - 1)
    print(N - ans[0])


if __name__ == '__main__':
    main()
