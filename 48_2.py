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
        dp = [[0] * N for _ in range(N)]  # 区間 [l, r] の dp

        for i in range(N - 1):
            if abs(w[i] - w[i + 1]) <= 1:
                dp[i][i + 1] = 2

        # dp 更新 --------------------------------
        for length in range(2, N):  # 区間長 - 1
            for l in range(N - length):
                r = l + length  # 区間 [l, r] の dp

                if length % 2 == 1:  # length が奇数 == 区間長が偶数の時
                    if dp[l + 1][r - 1] == length - 1 and (abs(w[l] - w[r]) <= 1):
                        dp[l][r] = length + 1
                        continue

                for k in range(l, r):
                    if dp[l][r] < dp[l][k] + dp[k + 1][r]:
                        dp[l][r] = dp[l][k] + dp[k + 1][r]

                        if (dp[l][r] == length + 1) or (dp[l][r] == length):  # 区間長が奇数ならばlength 区間長が偶数ならば lenght + 1 となる
                            break
        
        # for i in dp:
        #     print(i)

        print(dp[0][-1])


if __name__ == '__main__':
    main()
