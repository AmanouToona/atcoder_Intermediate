import pandas as pd
import numpy as np
import itertools

#
# def main():
#     N, M = map(int, input().split())
#     edge = [0]*N
#     for i in range(M):
#         x, y = map(int, input().split())
#         edge[x-1] |= 1 << (y-1)
#         print(f'y: {y}, {1 << (y - 1)}')
#
#     dp = [0] * (1 << N)
#     dp[0] = 1
#     for s in range(1, 1 << N):  # 集合を添字の小さい順に試す
#         for i in range(N):  # 全ての要素を考える
#             if ((s >> i) & 1) and (not(edge[i] & s)):  # i in sかつedge[i]とsが共通部分を持たない
#                 dp[s] += dp[s ^ (1 << i)]
#     return dp[-1]
#
#
# # print(main())
#
# for i in range(10):
#     print(f'i: {i}, 2 ** i: {2 ** i}, 1 << i: {1 << i}')


n, w = map(int, input().split())

# d[i][j]:i→jへの距離
d = [[float("inf")] * n for i in range(n)]
for i in range(w):
    x, y, z = map(int, input().split())
    d[x][y] = z

dp = [[-1] * n for i in range(1 << n)]


# 訪れた集合がs、今いる点がvの時０に戻る最短経路
def rec(s, v, dp):
    if dp[s][v] >= 0:
        return dp[s][v]

    if s == (1 << n) - 1 and v == 0:
        # 全ての頂点を訪れた(s = 11...11 and v = 0)
        dp[s][v] = 0
        return 0

    res = float("inf")
    for u in range(n):
        if (s >> u & 1) == 0:
            # uに訪れていない時(uの箇所が0の時),次はuとすると
            res = min(res, rec(s | (1 << u), u, dp) + d[v][u])

    dp[s][v] = res
    return res


print(rec(0, 0, dp))

for i in range(len(dp)):
    print(dp[i])





