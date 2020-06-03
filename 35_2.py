# DPL_1_B - 0,1ナップザック問題　
# 配るDPで解いてみる

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
    # dp[n + 1] = dp[n]  # python のリストは参照渡しなのでこの記法は使えない
    for c in range(C + 1):
        # dp[n + 1][c] = max(dp[n + 1][c], dp[n][c])  # すでに配られている可能性があるので max をとる

        if c + w[n] <= C:
            dp[n + 1][c + w[n]] = max(dp[n][c] + v[n], dp[n + 1][c + w[n]])

for i in range(len(dp)):
    print(dp[i])

ans = dp[-1][-1]
print(ans)
