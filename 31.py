# JOI 2012 予選 5 - イルミネーション

import sys
from collections import deque

W, H = map(int, sys.stdin.readline().strip().split())

# 移動は、 上下左右と斜め。　斜めは奇数行:
M = [[0] * (W + 2) for _ in range(H + 2)]  # Map
fp = [[True] * (W + 2) for _ in range(H + 2)]  # FootPrint

for h in range(H):
    m = list(map(int, sys.stdin.readline().strip().split()))
    for w, j in enumerate(m):
        if j == 1:
            M[h + 1][w + 1] = 1

# -----------------------------------------------------------------
q = deque()
q.append((0, 0))
fp[0][0] = False

ans_count = 0
while q:
    ux, uy = q.popleft()
    # print(f'ux: {ux}, uy: {uy}')
    # print(f'q: {q}')

    if uy % 2 == 0:
        for i in [[-1, -1], [0, -1], [-1, 0], [1, 0], [-1, 1], [0, 1]]:
            vx = ux + i[0]
            vy = uy + i[1]
            if (vx < 0) or (vx > W + 1):
                continue
            if (vy < 0) or (vy > H + 1):
                continue
            if fp[vy][vx] is False:
                continue
            if M[vy][vx] == 1:
                # print(f'vx; {vx}, vy: {vy}')
                ans_count += 1
                continue
            q.append((vx, vy))
            fp[vy][vx] = False

    else:
        for i in [[0, -1], [1, -1], [-1, 0], [1, 0], [0, 1], [1, 1]]:
            vx = ux + i[0]
            vy = uy + i[1]
            if (vx < 0) or (vx > W + 1):
                continue
            if (vy < 0) or (vy > H + 1):
                continue
            if fp[vy][vx] is False:
                continue
            if M[vy][vx] == 1:
                # print(f'vx: {vx}, vy: {vy}')
                ans_count += 1
                continue
            q.append((vx, vy))
            fp[vy][vx] = False

print(ans_count)

# for i in fp:
#     print(i)

