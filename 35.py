# DPL_1_B - 0,1ナップザック問題　

import sys

N, C = map(int, sys.stdin.readline().strip().split())  # C: content 容量

v, w = [], []
for _ in range(N):
    i, j = map(int, sys.stdin.readline().strip().split())
    v.append(i)
    w.append(j)

# dp 配列の初期化
dp = [[0] * (C + 1) for _ in range(N + 1)]


for n in range(N):
    for c in range(1, C + 1):
        if c >= w[n]:
            dp[n + 1][c] = max(dp[n][c - w[n]] + v[n], dp[n][c])
        else:
            dp[n + 1][c] = dp[n][c]


ans = dp[-1][-1]
print(ans)
