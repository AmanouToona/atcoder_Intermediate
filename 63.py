# AtCoder Beginner Contest 074 D - Restoring Road Network　

import sys

N = int(input())
A = []
for _ in range(N):
    a = list(map(int, sys.stdin.readline().strip().split()))
    b = a
    A.append(a)

needless = [[False] * N for _ in range(N)]

# ワーシャルフロイド
for k in range(N):
    for i in range(N):
        for j in range(N):
            if A[i][j] > A[i][k] + A[k][j]:
                print(-1)
                sys.exit()
            elif (A[i][j] == A[i][k] + A[k][j]) and (A[i][k] != 0) and (A[k][j] != 0):
                needless[i][j] = True

# for i in needless:
#     print(i)

ans = 0
for h in range(N):
    for w in range(N):
        if needless[h][w] is False:
            ans += A[h][w]

print(ans // 2)
