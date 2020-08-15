# JOI 2016 予選 5 - ゾンビ島　

import sys
import heapq

N, M, K, S = map(int, sys.stdin.readline().strip().split())
P, Q = map(int, sys.stdin.readline().strip().split())

dead_town = []
for _ in range(K):
    C = int(input())
    C -= 1
    dead_town.append(C)


G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().strip().split())
    A -= 1
    B -= 1

    G[A].append(B)
    G[B].append(A)


# ゾンビ町からの距離の演算 ---------------------------------------------------
dead_dist = [float('inf')] * N  # ゾンビ町までの距離
dead_que = []  # ゾンビ町からの距離を探索するためのキュー

for c in dead_town:
    heapq.heappush(dead_que, (0, c))

while dead_que:
    d_u, u = heapq.heappop(dead_que)

    if dead_dist[u] > d_u:
        dead_dist[u] = d_u
    else:
        continue

    for v in G[u]:
        heapq.heappush(dead_que, (d_u + 1, v))


# 答えを求める ------------------------------------------------------------
cost = [None] * N
cost[0] = 0

que = []
heapq.heappush(que, (0, 0))

ans = None
while que:
    if ans is not None:
        break

    d_u, u = heapq.heappop(que)

    if u == N -1:
        break

    for v in G[u]:
        if cost[v] is not None:  # 探索済みの町
            continue

        if v == N - 1:  # 目的地に到着
            ans = d_u
            break

        if dead_dist[v] > S:  # 安全な街
            heapq.heappush(que, (d_u + P, v))
            cost[v] = d_u + P
        elif dead_dist[v] != 0:  # 危険な街
            heapq.heappush(que, (d_u + Q, v))
            cost[v] = d_u + Q
        else:  # ゾンビのいる町
            continue

print(ans)
