# AtCoder Beginner Contest 007 C - 幅優先探索

import sys
import heapq

R, C = map(int, sys.stdin.readline().strip().split())
sy, sx = map(int, sys.stdin.readline().strip().split())
gy, gx = map(int, sys.stdin.readline().strip().split())

fp = []  # 探索可能か記録する
q = []  # heap
heapq.heapify(q)


for _ in range(R):
    c = str(input())
    c = [True if i == '.' else False for i in c]
    fp.append(c)

ans = -1

heapq.heappush(q, (0, sx - 1, sy - 1))  # key は距離
fp[sy - 1][sx - 1] = False
while q:
    d, ux, uy = heapq.heappop(q)
    d += 1

    for i in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        vx = ux + i[0]
        vy = uy + i[1]
        # print(f'vx: {vx} vy: {vy}')

        if (vx < 0) or (vx >= C):
            continue
        if (vy < 0) or (vy >= R):
            continue
        if fp[vy][vx] is False:
            continue

        if (vx == gx - 1) and (vy == gy - 1):
            ans = d
            break

        heapq.heappush(q, (d, vx, vy))
        fp[vy][vx] = False
    else:
        continue
    break

print(ans)
