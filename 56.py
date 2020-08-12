import sys
import heapq

V, E, r = map(int, sys.stdin.readline().strip().split())

G = [[] for _ in range(V)]
for e in range(E):
    s, t, d = map(int, sys.stdin.readline().strip().split())

    G[s].append((t, d))
    # G[t].append((s, d))


distance = ['INF'] * V  # 何らかの数値: 探索済み  INF: 未探索
distance[r] = 0
que = []

for u, d_u in G[r]:
    heapq.heappush(que, (d_u, u))

while que:
    d_tot, u = heapq.heappop(que)
    if distance[u] is not 'INF':
        continue

    distance[u] = d_tot
    for v, d_v in G[u]:
        if distance[v] is not 'INF':  # v にすでに訪問済みであった場合
            continue
        heapq.heappush(que, (d_tot + d_v, v))

for i in distance:
    print(i)