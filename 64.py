# GRL_2_A - 最小全域木
import sys
import heapq

V, E = map(int, sys.stdin.readline().strip().split())
G = [[] for _ in range(V)]

for _ in range(E):
    s, t, w = map(int, sys.stdin.readline().strip().split())
    G[s].append((w, t))
    G[t].append((w, s))

q = []
fp = [False] * V

for v in G[0]:
    heapq.heappush(q, v)
fp[0] = True

total_d = 0
while q:
    d, v = heapq.heappop(q)

    if fp[v] is False:  # 未到達地点ならば
        total_d += d
        fp[v] = True
        for v in G[v]:
            if fp[v[1]] is False:
                heapq.heappush(q, v)

print(total_d)        
