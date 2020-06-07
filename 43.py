# パ研杯2019 D - パ研軍旗

import sys

N = int(input())
S = [[] for _ in range(N)]  # 縦横を逆にして保持した方が後で扱いやすい
for _ in range(5):
    s = list(map(str, sys.stdin.readline().strip()))
    for i, ss in enumerate(s):
        S[i].append(ss)


# R, B, W = 0, 1, 2 として　配るDP　で解く
dp = [[float('inf')] * 3 for _ in range(N)]  # N列の旗 * 3色塗分け

# 初期値の計算
dp[0][0] = sum([0 if i == 'R' else 1 for i in S[0]])  # 旗の一番端の列の R:1 への塗りなおしコストの計算
dp[0][1] = sum([0 if i == 'B' else 1 for i in S[0]])  # 旗の一番端の列の B:2 への塗りなおしコストの計算
dp[0][2] = sum([0 if i == 'W' else 1 for i in S[0]])  # 旗の一番端の列の W:3 への塗りなおしコストの計算


for n in range(N - 1):  # 配るDP
    for color in range(3):
        # 旗の端から n + 1 列目の color への塗りなおしコストの計算
        color_dict = {0: 'R', 1: 'B', 2: 'W'}
        cost = sum([0 if i == color_dict[color] else 1 for i in S[n + 1]])
        # print(f'color: {color}, cost: {cost}')

        for j in range(3):
            if color == j:
                continue
            dp[n + 1][color] = min(dp[n + 1][color], dp[n][j] + cost)

# for i in range(len(dp)):
#     print(dp[i])

print(min(dp[-1]))
