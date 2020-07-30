# DPL_2_A - 巡回セールスマン問題
# 配る DP で書いてみる

import sys
sys.setrecursionlimit(10 ** 8)

V, E = map(int, sys.stdin.readline().strip().split())
d = [[float('inf')] * V for _ in range(V)]
for _ in range(E):
    s, t, _d = map(int, sys.stdin.readline().strip().split())
    d[s][t] = _d

# dp 初期化 -----------------
dp = [[float('inf')] * V for _ in range(1 << V)]  # 1 << V は 2 ** V に同じ
dp[0][0] = 0

# dp --------------------------
for s in range(1 << V):
    for v in range(V):
        for u in range(V):
            # dp[s][] = min()
            # dp[s][v] = min(dp[s | (1 << v)][u] + d[u][v], dp[s][v])
            pass
        pass



