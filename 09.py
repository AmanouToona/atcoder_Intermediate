# JOI 2008 予選 4 - 星座探し

import sys

m = int(input())  # 探したい星座を構成する星の数
asterism1 = []  # 探したい星座の座標
for _ in range(m):
    x, y = map(int, sys.stdin.readline().strip().split())
    asterism1.append([x, y])
asterism1 = sorted(asterism1, key=lambda x: x[0])

n = int(input())  # 写真に写っている星の数
asterism2 = []  # 写真に写っている星の座標
for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    asterism2.append([x, y])
asterism2 = sorted(asterism2, key=lambda x: x[0])

slide_x, slide_y = 0, 0
find = False

for x2, y2 in asterism2:
    slide_x = x2 - asterism1[0][0]
    slide_y = y2 - asterism1[0][1]
    for x1, y1 in asterism1:
        if [x1 + slide_x, y1 + slide_y] in asterism2:
            find = True
        else:
            find = False
            break
    if find:
        break

print(slide_x, slide_y)
