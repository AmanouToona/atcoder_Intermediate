# ALDS_11_C - 幅優先探索
import sys
import heapq

N = int(input())
G = []
for _ in range(N):
    u, k, *v = map(int, sys.stdin.readline().strip().split())
    v = [i - 1 for i in v]
    G.append(v)


distance = [-1] * N
q = []
fp = [True] * N  # 探索可能か記録する
heapq.heapify(q)
heapq.heappush(q, (0, 0))
fp[0] = False


while q:
    dist, u = heapq.heappop(q)
    distance[u] = dist
    for v in G[u]:
        if fp[v] is True:
            heapq.heappush(q, (dist + 1, v))
            fp[v] = False

for i, d in enumerate(distance):
    print(i + 1, d)
