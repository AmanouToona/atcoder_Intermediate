# AOJ 2199 - 差分パルス符号変調
# 配るDP
import sys


def main():
    while True:
        N, M = map(int, sys.stdin.readline().strip().split())

        if (N == 0) and (M == 0):
            break

        C = list()
        for _ in range(M):
            C.append(int(sys.stdin.readline()))
        x = list()
        for _ in range(N):
            x.append(int(sys.stdin.readline()))

        # dp 初期化 ---------------------------------------------------------
        dp = [[float('inf')] * 256 for _ in range(N + 1)]
        dp[0][128] = 0  # 初期信号　y0 = 128

        error_list = tuple(tuple((i - j) ** 2 for i in range(256)) for j in range(256))
        decode_list = tuple(tuple(255 if j + c > 255 else 0 if j + c < 0 else j + c for c in C) for j in range(256))

        # dp 計算 ---------------------------------------------------------
        for i in range(N):
            for j in range(256):
                if dp[i][j] == float('inf'):
                    continue
                for x_decode in decode_list[j]:

                # decode_list を使わない方法　遅い
                # for c in C:
                #     x_decode = int(j + c)

                    # x_decode は自動的に 0<= x_decode <= 255 に丸められる
                    # if x_decode < 0:
                    #     x_decode = 0
                    # elif x_decode > 255:
                    #     x_decode = 255

                    # error = error_list[x[i]][x_decode]
                    new_sum_error = dp[i][j] + error_list[x[i]][x_decode]

                    if new_sum_error < dp[i + 1][x_decode]:
                        dp[i + 1][x_decode] = new_sum_error

        # for i in range(len(dp)):
        #     print(dp[i])

        ans = min(dp[-1])
        print(ans)


if __name__ == '__main__':
    main()

