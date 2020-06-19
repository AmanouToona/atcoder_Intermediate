# Square869120Contest #1 G - Revenge of Traveling Salesman Problem

import sys

# 入力受け
N, M = map(int, sys.stdin.readline().strip().split())
d = [[float('inf')] * N for _ in range(N)]
for _ in range(M):
    s, t, _d, time = map(int, sys.stdin.readline().strip().split())
    d[s - 1][t - 1] = (_d, time)
    d[t - 1][s - 1] = (_d, time)

# dp 用意
dp = [[None] * N for _ in range(1 << N)]


def res(s, v, t, dp):
    # s: 訪問した店の集合, v: 今いる店, t: 現在時刻
    # 経路は封鎖前に渡り終えねばならない

    if (s == (1 << N - 1)) and (v == 0):
        dp[s][v] = (0, float('inf'))
        return dp[s][v]

    if dp[s][v] is not None:
        # 現在時刻でこの経路が使用可能か判断する必要がある。
        d_cost, t_limit = dp[s][v]
        if t > t_limit:
            return None
        else:
            return dp[s][v]


#



