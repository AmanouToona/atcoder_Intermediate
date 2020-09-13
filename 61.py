# AtCoder Beginner Contest 012 D - バスと避けられない運命

import sys

# 入力
N, M = map(int, sys.stdin.readline().strip().split())

G = [[float('inf')] * N for _ in range(N)]
for n in range(N):
    G[n][n] = 0

for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().strip().split())
    a -= 1
    b -= 1

    G[a][b] = t
    G[b][a] = t

# ワーシャルフロイド
for k in range(N):
    for i in range(N):
        for j in range(N):
            G[i][j] = min(G[i][j], G[i][k] + G[k][j])

# 各地点を出発したとき、バスに乗らなければならない最大時間を計算
max_time = [max(g) for g in G]

# 答えは バスに乗らなければならない最大時間の最小値
ans = min(max_time)

# 出力
print(ans)
