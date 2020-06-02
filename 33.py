# AtCoder Beginner Contest 088 D - Grid Repainting

import sys
from collections import deque

H, W = map(int, sys.stdin.readline().strip().split())
S = []
start_counter = 0  # 始状態の # をカウントする
for _ in range(H):
    s = list(map(str, sys.stdin.readline()))
    S.append(s)
    for i in s:
        if i == '#':
            start_counter += 1


# 幅優先で最短経路を探索　最短経路で通る白ますの数を求める
fp = [[True] * W for _ in range(H)]  # FootPrint 探索済みか記録する
q = deque()
q.append((0, 0, 1))
fp[0][0] = False

ans_counter = -1
while q:
    ux, uy, counter = q.popleft()
    # print(f'ux: {ux}, uy: {uy}, counter: {counter}')

    if (ux == W - 1) and (uy == H - 1):
        ans_counter = counter
        break

    for i in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        vx = ux + i[0]
        vy = uy + i[1]

        if (vx < 0) or (vx >= W):
            continue
        if (vy < 0) or (vy >= H):
            continue
        if fp[vy][vx] is False:
            continue
        if S[vy][vx] == '#':
            continue

        q.append((vx, vy, counter + 1))
        fp[vy][vx] = False

if ans_counter == -1:
    print(-1)
else:
    print(H * W - start_counter - ans_counter)
