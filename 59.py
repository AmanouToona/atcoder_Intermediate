# JOI 2014 予選 5 - タクシー

import sys
import heapq

# 入力
N, K = map(int, sys.stdin.readline().strip().split())  # N: 町の数  K: 道路の本数

Taxi = []
for n in range(N):
    C, R = map(int, sys.stdin.readline().strip().split())  # C: 運賃 R: 通過可能な道路の本数
    Taxi.append((C, R))

G_in = [[] for _ in range(N)]
for k in range(K):
    A, B = map(int, sys.stdin.readline().strip().split())  # A, B : 道路の存在する町同士
    A -= 1
    B -= 1

    G_in[A].append(B)
    G_in[B].append(A)

# ---------------------------------------------------------------------------
# 各町のタクシーが到達可能な街をグラフに追加する
G = [[] for _ in range(N)]
for i, g in enumerate(G_in):
    fp = [False] * N  # 到達済みの町かを記録する
    fp[i] = True  # 探索開始地点は到達済み

    q = []
    for gg in g[:]:
        if Taxi[i][1] > 0:
            heapq.heappush(q, (1, gg))
            G[i].append(gg)
            fp[gg] = True

    while q:
        cost, u = heapq.heappop(q)

        if cost + 1 <= Taxi[i][1]:
            for v in G_in[u]:
                if fp[v]:
                    continue
                heapq.heappush(q, (cost + 1, v))
                fp[v] = True
                G[i].append(v)
del G_in

# 地図が完成したので ダイクストラで解く
q = []
price = [float('inf')] * N  # 各町までの運賃
price[0] = 0

for u in G[0]:
    heapq.heappush(q, (Taxi[0][0], u))
    price[u] = Taxi[0][0]

ans = None
while q:
    u_cost, u = heapq.heappop(q)
    if u == N - 1:
        ans = u_cost
        break

    for v in G[u]:
        if price[v] > u_cost + Taxi[u][0]:
            price[v] = u_cost + Taxi[u][0]
            heapq.heappush(q, (u_cost + Taxi[u][0], v))

print(ans)
