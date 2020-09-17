# AOJ 1127 - Building a Space Station
import sys
import heapq

while True:
    # input -----------------------
    n = int(input())  # <= 100
    if n == 0:
        break

    input_list = []
    for _ in range(n):
        # x, y, z 座標と 半径r  <= 100 小数点以下3桁
        x, y, z, r = map(float, sys.stdin.readline().strip().split())
        input_list.append((x, y, z, r))

    # make adjacency matrix ---------------------
    G = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        x1, y1, z1, r1 = input_list[i]

        for j in range(i, n):
            x2, y2, z2, r2 = input_list[j]
            
            d = ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5 - (r1 + r2)
            d = max(0, d)

            G[i][j] = d
            G[j][i] = d

    # calc minimum spanning tree ----------
    q = []
    fp = [False] * n  # foot print
    fp[0] = True
    for i, d in enumerate(G[0]):
        if i == 0:
            continue
        heapq.heappush(q, (d, i))

    ans_dist = 0
    while q:
        d, u = heapq.heappop(q)

        if fp[u]:
            continue
        
        ans_dist += d
        fp[u] = True

        for v, d in enumerate(G[u]):
            if fp[v]:
                continue
            heapq.heappush(q, (d, v))

    print(f'{ans_dist:.3f}')
