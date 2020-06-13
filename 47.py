# JOI 2015 本選 2 - ケーキの切り分け 2

import sys

N = int(input())
A = []
for _ in range(N):
    A.append(int(sys.stdin.readline().strip()))

# dp 初期化 ------------------------------------------------------------------------------------------------------------
dp = [[0] * N for _ in range(N)]

if N % 2 == 1:
    for n in range(N):
        dp[n][n] = A[n]

# dp 更新 --------------------------------------------------------------------------------------------------------------
ans = 0
for l in range(1, N):
    for i in range(N):
        j = i + l
        remain = l + 1
        if remain % 2 == N % 2:  # 残りのケーキと切り分け数 N の偶奇が一致するとき JOI の番
            dp[i][j % N] = max(dp[i][(j - 1) % N] + A[j % N], dp[(i + 1) % N][j % N] + A[i])

        # IOI の番
        elif A[i] < A[j % N]:
            dp[i][j % N] = dp[i][(j - 1) % N]
        else:
            dp[i][j % N] = dp[(i + 1) % N][j % N]

        if (l == N - 1) & (ans < dp[i][j % N]):
            ans = dp[i][j % N]

# for i in range(len(dp)):
    # print(dp[i])

print(ans)
