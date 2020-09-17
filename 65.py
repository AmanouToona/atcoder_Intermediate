# finals - 本選会場 (Finals) 
import sys
import heapq

N, M, K = map(int, sys.stdin.readline().strip().split())

G = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().strip().split())
    A -= 1
    B -= 1
    G[A].append((C, B))
    G[B].append((C, A))

fp = [False] * N
q = []

for g in G[0]:
    heapq.heappush(q, g)
fp[0] = True

dist = []
while q:
    d, v = heapq.heappop(q)

    if fp[v] is False:
        fp[v] = True
        dist += [d]
        
        for g in G[v]:
            if fp[g[1]] is True:
                continue

            heapq.heappush(q, g) 

print(sum(sorted(dist)[:(N - K)]))
