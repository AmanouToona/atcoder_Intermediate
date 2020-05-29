# AtCoder Beginner Contest 138 D - Ki　
import sys
sys.setrecursionlimit(10 ** 9)

N, Q = map(int, sys.stdin.readline().strip().split())

M = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    M[a - 1].append(b - 1)
    M[b - 1].append(a - 1)

X = [0] * N
for _ in range(Q):
    p, x = map(int, sys.stdin.readline().strip().split())
    X[p - 1] += x


ans = [0] * N


def dfs(u, parent=None):

    ans[u] = ans[parent] + X[u]

    for v in M[u]:
        if v != parent:
            dfs(v, u)


dfs(0, 0)
print(' '.join([str(i) for i in ans]))
