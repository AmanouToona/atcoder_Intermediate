# AtCoder Beginner Contest 002 D - 派閥

import sys

N, M = map(int, sys.stdin.readline().strip().split())

K = [[0] * N for _ in range(N)]  # 議員間の関係
for i in range(N):
    K[i][i] = 1

for _ in range(M):
    x, y = map(int, sys.stdin.readline().strip().split())
    K[x - 1][y - 1] = 1
    K[y - 1][x - 1] = 1

ans = 0
for i in range(2 ** N):
    bit = [(i >> j) & 1 for j in range(N)]
    edges = 0
    for i, b in enumerate(bit):
        if b == 0:
            continue
        edges += sum([x * y for x, y in zip(K[i], bit)])
    if edges == sum(bit) ** 2:
        ans = max(ans, sum(bit))

print(ans)

