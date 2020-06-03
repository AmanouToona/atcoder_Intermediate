# DPL_1_A - コイン問題　

import sys

N, M = map(int, sys.stdin.readline().strip().split())  # N払う　コイン種類M 枚
c = list(map(int, sys.stdin.readline().strip().split()))

# dp 初期化
dp = [[float('inf')] * (N + 1) for _ in range(M + 1)]
for i in range(len(dp)):
    dp[i][0] = 0


for m in range(M):
    for n in range(N + 1):
        dp[m + 1][n] = min(dp[m + 1][n], dp[m][n])
        next_n = n + c[m]
        if next_n <= N:
            dp[m + 1][next_n] = min(dp[m + 1][n] + 1, dp[m][next_n])


# for i in range(len(dp)):
#     print(dp[i])

print(dp[-1][-1])
