# AOJ 1166 - 迷図と命ず

import sys
from collections import deque

while True:
    W, H = map(int, sys.stdin.readline().strip().split())

    if (W == 0) and (H == 0):
        break

    Ph = []  # Partition horizontal  H * (W -1)  横移動を遮る仕切り
    Pv = []  # Partition vertical  (H - 1) * W  縦移動を遮る仕切り

    for h in range(2 * H - 1):
        p = list(map(int, sys.stdin.readline().strip().split()))
        if h % 2 == 0:
            Ph.append(p)
        else:
            Pv.append(p)

    # ----------------------------------------------------
    fp = [[True] * W for _ in range(H)]  # FootPrint  探索済みか判断する

    q = deque()
    counter = 1
    q.append((0, 0, counter))
    fp[0][0] = False

    ans_counter = 0
    while q:
        flag = False
        ux, uy, counter = q.popleft()
        # print(f'ux: {ux}, uy: {uy}, counter: {counter}')

        if (ux == W - 1) and (uy == H -1):
            ans_counter = counter
            break

        for i in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            vx = ux + i[0]
            vy = uy + i[1]
            # print(f'vx: {vx} vy: {vy}')

            if (vx < 0) or (vx >= W):
                continue
            if (vy < 0) or (vy >= H):
                continue
            if fp[vy][vx] is False:
                continue
            # print(f'vx: {vx}, vy: {vy}')

            if (i[1] == 1) and (Pv[uy][ux] == 0):  # 縦方向の移動　下
                q.append((vx, vy, counter + 1))
                fp[vy][vx] = False
            elif (i[1] == -1) and (Pv[vy][ux] == 0):  # 縦方向の移動　上
                q.append((vx, vy, counter + 1))
                fp[vy][vx] = False
            elif (i[0] == 1) and (Ph[uy][ux] == 0):  # 横方向の移動　右
                q.append((vx, vy, counter + 1))
                fp[vy][vx] = False
            elif (i[0] == -1) and (Ph[uy][vx] == 0):  # 横方向の移動　左
                q.append((vx, vy, counter + 1))
                fp[vy][vx] = False

    print(ans_counter)
