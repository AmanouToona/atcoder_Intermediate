# ALDS_10_B - 連鎖行列積

import sys

N = int(input())

M = []
for n in range(N):
    r, c = map(int, sys.stdin.readline().strip().split())
    if n == 0:
        M.append(r)
    M.append(c)


# dp 初期化
dp = [[float('inf')] * N for _ in range(N)]
for n in range(N):
    dp[n][n] = 0

# dp 更新
for l in range(1, N):
    for i in range(N - l):
        j = i + l
        for k in range(i, j):
            # print(f'k: {k}, i: {i}, j: {j}')
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + M[i] * M[k + 1] * M[j + 1])

# for i in range(len(dp)):
#     print(dp[i])

print(dp[0][N - 1])
