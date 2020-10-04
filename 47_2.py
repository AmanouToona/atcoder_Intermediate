# JOI 2015 本選 2 - ケーキの切り分け 2
import sys

# input -------------
N = int(input())
A = []

for n in range(N):
    A.append(int(sys.stdin.readline().strip()))

# dp 初期化 -------------
# dp は [l, r) の区間が残っているときに JOI がとりえる最大のケーキの面積とする
dp = [[0] * N for _ in range(N)]

if N % 2 == 1:
    for n in range(N):
        dp[n][(n + 1) % N] = A[n]

# dp 更新 -----------------
for remain in range(2, N + 1):  # 残っているケーキの量で探索をかける
    for l in range(N):
        r = l + remain  # [l, r)

        if remain % 2 == N % 2:  # JOI のターン
            dp[l][r % N] = max(dp[l][(r - 1) % N] + A[(r - 1) % N],
                               dp[(l + 1) % N][r % N] + A[l])
        else:  # IOI のターン
            if A[(r - 1) % N] > A[l]:
                dp[l][r % N] = dp[l][(r - 1) % N]
            else:
                dp[l][r % N] = dp[(l + 1) % N][r % N]

ans = 0
for i in range(N):
    if ans < dp[i][i]:
        ans = dp[i][i]

print(ans)
