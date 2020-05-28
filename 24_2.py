# ALDS_11_B - 深さ優先探索
import sys

n = int(input())
e = [None] * n
for _ in range(n):
    u, k, *v = map(int, sys.stdin.readline().strip().split())
    e[u - 1] = [i - 1 for i in v]

S = []  # stack
time = 0
t_in = [0] * n
t_out = [0] * n
fp = [False] * n  # foot print  訪問の記録


def dfs(u):
    global time
    fp[u] = True
    time += 1
    t_in[u] = time
    for v in e[u]:
        if fp[v] is False:
            dfs(v)
    time += 1
    t_out[u] = time


while False in fp:
    dfs(fp.index(False))

for i in range(n):
    print(f'{i + 1} {t_in[i]} {t_out[i]}')
