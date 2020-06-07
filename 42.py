# JOI 2015 予選 4 - シルクロード

import sys

N, M = map(int, sys.stdin.readline().strip().split())

D = []
for n in range(N):
    D.append(int(input()))

C = []
for m in range(M):
    C.append(int(input()))

dp = [[float('inf')] * (N + 1) for _ in range(M + 1)]
dp[0][0] = 0

for m in range(M):  # 配るDP
    for n in range(N + 1):
        if n > m:
            break

        dp[m + 1][n] = min(dp[m + 1][n], dp[m][n])
        if n + 1 < N + 1:
            dp[m + 1][n + 1] = min(dp[m + 1][n + 1], dp[m][n] + C[m] * D[n])

# for i in range(len(dp)):
#     print(dp[i])

print(dp[-1][-1])

