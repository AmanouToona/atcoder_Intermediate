# JOI 2011 本選 1 - 惑星探査
import sys

M, N = map(int, sys.stdin.readline().strip().split())
K = int(input())

graph = []
for _ in range(M):
    g = list(str(input()))
    graph.append(g)

# 2次元累積和の用意
J = [[0] * (N + 1) for _ in range(M + 1)]
O = [[0] * (N + 1) for _ in range(M + 1)]
I = [[0] * (N + 1) for _ in range(M + 1)]

for i in range(M):
    for j in range(N):
        J[i + 1][j + 1] = J[i + 1][j]
        O[i + 1][j + 1] = O[i + 1][j]
        I[i + 1][j + 1] = I[i + 1][j]

        if graph[i][j] == 'J':
            J[i + 1][j + 1] += 1
        elif graph[i][j] == 'O':
            O[i + 1][j + 1] += 1
        elif graph[i][j] == 'I':
            I[i + 1][j + 1] += 1

for i in range(M):
    for j in range(N):
        J[i + 1][j + 1] += J[i][j + 1]
        O[i + 1][j + 1] += O[i][j + 1]
        I[i + 1][j + 1] += I[i][j + 1]

# 回答
for _ in range(K):
    a, b, c, d = map(int, sys.stdin.readline().strip().split())
    j = J[c][d] - (J[a - 1][d] - J[a - 1][b - 1]) - (J[c][b - 1] - J[a - 1][b - 1]) - J[a - 1][b - 1]
    o = O[c][d] - (O[a - 1][d] - O[a - 1][b - 1]) - (O[c][b - 1] - O[a - 1][b - 1]) - O[a - 1][b - 1]
    i = I[c][d] - (I[a - 1][d] - I[a - 1][b - 1]) - (I[c][b - 1] - I[a - 1][b - 1]) - I[a - 1][b - 1]

    print(f'{j} {o} {i}')
