# GRL_1_C - 全点対間最短経路　

import sys

# 入力
V, E = map(int, sys.stdin.readline().strip().split())

G = [[float('inf')] * V for _ in range(V)]
for v in range(V):
    G[v][v] = 0
for _ in range(E):
    s, t, d = map(int, sys.stdin.readline().strip().split())
    G[s][t] = d

# ワーシャルフロイド
for k in range(V):
    for i in range(V):
        for j in range(V):
            G[i][j] = min(G[i][j], G[i][k] + G[k][j])

# 負閉路探索 出力
for v in range(V):
    if G[v][v] < 0:
        print('NEGATIVE CYCLE')
        sys.exit()

# 出力
for y in range(V):
    for x in range(V):
        if G[y][x] != float('inf'):
            print(G[y][x], end='')
        else:
            print('INF', end='')

        if x != V - 1:
            print(' ', end='')

    print('')
