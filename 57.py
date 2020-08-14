import sys
import heapq

n, k = map(int, sys.stdin.readline().strip().split())

G = [[] for _ in range(n)]

for _ in range(k):
    # print('G', G)
    id, *l = map(int, sys.stdin.readline().strip().split())

    if id == 0:  # 注文処理
        a, b = l
        a -= 1
        b -= 1

        que = []
        for g in G[a]:
            v, d_v = g
            heapq.heappush(que, (d_v, v))

        dists = [float('inf')] * n
        while que:
            d_u, u = heapq.heappop(que)

            if dists[u] != float('inf'):
                continue

            dists[u] = d_u

            if u == b:
                break

            for v, d_v in G[u]:
                if dists[v] is float('inf'):
                    continue
                heapq.heappush(que, (d_u + d_v, v))

        if dists[b] != float('inf'):
            # print('dists[b]', dists[b])
            print(dists[b])
        else:
            print(-1)

    else:  # 運行情報
        c, d, e = l
        c -= 1
        d -= 1
        G[c].append((d, e))
        G[d].append((c, e))

