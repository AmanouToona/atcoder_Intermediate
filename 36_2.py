# DPL_1_B - 0,1ナップザック問題
# 貰う DP で回答

import sys
import math

N, W = map(int, sys.stdin.readline().strip().split())

item = []
for n in range(N):
    v, w = map(int, sys.stdin.readline().strip().split())
    item.append((v, w))


# dp 準備
dp = [[0] * (W + 1) for _ in range(N + 1)]

# dp 実行
for n in range(N):
    for w in range(W + 1):
        if w - item[n][1] >= 0:
            dp[n + 1][w] = max(dp[n][w], dp[n + 1][w - item[n][1]] + item[n][0])
        else:
            dp[n + 1][w] = dp[n][w]


# for i in range(len(dp)):
#     print(dp[i])

print(dp[-1][-1])
