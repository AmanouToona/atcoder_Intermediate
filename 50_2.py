# Square869120Contest #1 G - Revenge of Traveling Salesman Problem
# 貰うDP

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
dp = [[[None, 0] for _ in range(N)] for _ in range(1 << N)]


def res(s, v):
    # s: 訪問した店の集合, v: 今いる店, dp: 総移動距離 = 必要時間を記録する
    # 経路は封鎖前に渡り終えねばならない

    if dp[s][v][0] is not None:
        return

    if (s ^ (1 << v)) == 0:  # 終端の条件
        distance, time_limit = d[0][v]
        if distance is None:
            dp[s][v][0] = float('inf')
            return
        if distance <= time_limit:
            dp[s][v][0] = distance
            dp[s][v][1] = 1
            return

    ans = float('inf')
    for u in range(N):  # u: 直前の店
        if u == v:
            continue

        if (s >> u & 1) == 1:  # u に訪問済
            distance, time_limit = d[u][v]
            if distance is None:
                continue

            res(s ^ (1 << v), u)

            if dp[s ^ (1 << v)][u][0] + distance > time_limit:  # 道が封鎖されている
                continue

            if dp[s ^ (1 << v)][u][0] + distance == ans:
                dp[s][v][1] += dp[s ^ (1 << v)][u][1]
            elif dp[s ^ (1 << v)][u][0] + distance < ans:
                dp[s][v][1] = dp[s ^ (1 << v)][u][1]

            ans = min(ans, dp[s ^ (1 << v)][u][0] + distance)

    dp[s][v][0] = ans

    return


res(2 ** N - 1, 0)

# for i in range(len(dp)):
#     print(dp[i])


if dp[2 ** N - 1][0][0] == float('inf'):
    print('IMPOSSIBLE')
else:
    print(dp[2 ** N - 1][0][0], dp[2 ** N - 1][0][1])
