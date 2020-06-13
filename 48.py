# AOJ 1611 ダルマ落とし
# 貰うdp

import sys


def main():
    while True:
        N = int(input())
        if N == 0:
            break
        w = list(map(int, sys.stdin.readline().strip().split()))

        # dp 初期化 -------------------------------------------------
        dp = [[0] * N for _ in range(N)]

        for i in range(N - 1):
            if abs(w[i] - w[i + 1]) <= 1:
                dp[i][i + 1] = 2

        # dp 更新 ------------------------------------------------------
        for l in range(2, N):
            for i in range(N - l):
                j = i + l

                if l % 2 == 1:  # この条件を入れないと TLE する
                    if dp[i + 1][j - 1] == l - 1 and (abs(w[i] - w[j]) <= 1):
                        dp[i][j] = l + 1
                        continue

                for k in range(i, j):
                    if dp[i][j] < dp[i][k] + dp[k + 1][j]:
                        dp[i][j] = dp[i][k] + dp[k + 1][j]
                        if dp[i][j] == l:  # 枝刈入れないと TLE する
                            break

        # for i in range(len(dp)):
        #     print(dp[i])

        print(dp[0][-1])


if __name__ == '__main__':
    main()
