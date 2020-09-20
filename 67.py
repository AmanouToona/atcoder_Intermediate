# D - Built?
import sys
import heapq

# input
N = int(input())

X, Y = [], []
for n in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    X.append((x, n))
    Y.append((y, n))

# build matrix
G = [[] for _ in range(N)]

X.sort()
Y.sort()
for i in range(N - 1):
    d_u, u = X[i]
    d_v, v = X[i + 1]

    G[u].append((d_v - d_u, v))
    G[v].append((d_v - d_u, u))

    d_u, u = Y[i]
    d_v, v = Y[i + 1]

    G[u].append((d_v - d_u, v))
    G[v].append((d_v - d_u, u))


# 最小全域木
q = []
fp = [False] * N  # 探索済み
fp[0] = True

for d, u in G[0]:
    heapq.heappush(q, (d, u))

ans = 0
while q:
    d, u = heapq.heappop(q)

    if fp[u]:
        continue
    fp[u] = True
    ans += d

    for d_v, v in G[u]:
        if fp[v]:
            continue
        heapq.heappush(q, (d_v, v))

print(ans)
