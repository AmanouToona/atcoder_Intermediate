# AtCoder Beginner Contest 079 D - Wall

import sys

H, W = map(int, sys.stdin.readline().strip().split())
C = []
for _ in range(10):
    c = list(map(int, sys.stdin.readline().strip().split()))
    C.append(c)

A = []
for h in range(H):
    a = list(map(int, sys.stdin.readline().strip().split()))
    A.append(a)

# コストをワーシャルフロイド
for k in range(10):
    for i in range(10):
        for j in range(10):
            C[i][j] = min(C[i][j], C[i][k] + C[k][j])

# 必要なコストは、各数字を1 に変化させる部分のみなので
cost = [c[1] for c in C]

# 壁の数字を順番に探索して必要なコストを足していく
ans = 0
for h in range(H):
    for w in range(W):
        # 壁に数字が存在しないとき
        if A[h][w] == -1:
            continue
        ans += cost[A[h][w]]

print(ans)
