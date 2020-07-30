# Square869120Contest #1 G - Revenge of Traveling Salesman Problem
# 配るDP

import sys
sys.setrecursionlimit(10 ** 8)

# 入力受け
N, M = map(int, sys.stdin.readline().strip().split())
d = [[(None, None)] * N for _ in range(N)]
for _ in range(M):
    s, t, _d, time = map(int, sys.stdin.readline().strip().split())
    d[s - 1][t - 1] = (_d, time)
    d[t - 1][s - 1] = (_d, time)

# dp 用意
dp = [[None] * N for _ in range(1 << N)]


def res(s, v, dp):
    # s: 訪問した店の集合, v: 今いる店, dp: 総移動距離 = 必要時間を記録する
    # 経路は封鎖前に渡り終えねばならない

    if (s == (1 << (N - 1))) and (v == 0):
        return

    ans = float('inf')
    for u in range(N):  # u: 次に移動する店
        if (s >> u & 1) == 0:  # u にまだ訪問していない
            distance, time_limit = d[v][u]
            if distance is None:
                continue
            if dp[s][v] + distance > time_limit:
                continue

            ans = min(ans, dp[s][v] + distance)

