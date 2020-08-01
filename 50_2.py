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
dp = [[None] * N for _ in range(1 << N)]
counter = 0


def res(s, v):
    global counter
    # s: 訪問した店の集合, v: 今いる店, dp: 総移動距離 = 必要時間を記録する
    # 経路は封鎖前に渡り終えねばならない
    # print(f'res called s:{format(s, "b")}, v:{v}')

    if dp[s][v] is not None:
        return dp[s][v]

    if (s ^ (1 << v)) == 0:  # 終端の条件
        distance, time_limit = d[0][v]
        if distance is None:
            dp[0][v] = float('inf')
            return dp[0][v]
        if distance <= time_limit:
            dp[0][v] = distance
            return dp[0][v]

    ans = float('inf')
    for u in range(N):  # u: 直前に店
        if u == v:
            continue

        if (s >> u & 1) == 1:  # u に訪問済

            # print(f"s: {format(s, 'b')}, u: {u}")

            distance, time_limit = d[u][v]
            if distance is None:
                continue

            if res(s ^ (1 << v), u) + distance > time_limit:  # 道が封鎖されている
                continue

            if v == 0:
                if res(s ^ (1 << v), u) + distance == ans:
                    counter += 1
                elif res(s ^ (1 << v), u) + distance < ans:
                    counter = 1

            ans = min(ans, res(s ^ (1 << v), u) + distance)

        # if ans and v == 0:
        #     counter += 1

    dp[s][v] = ans

    return ans


ans = res(2 ** N - 1, 0)

# for i in range(len(dp)):
#     print(dp[i])


if ans == float('inf'):
    print('IMPOSSIBLE')
else:
    print(ans, counter)
