# ALDS_11_B - 深さ優先探索
import sys

n = int(input())
e = [None] * n
for _ in range(n):
    u, k, *v = map(int, sys.stdin.readline().strip().split())
    e[u - 1] = v

# print(e)

S = []  # stack
time = 0
t_in = [0] * n
t_out = [0] * n
fp = [False] * n  # foot print  訪問の記録


def dfs(u):
    global time

    fp[u] = True
    S.append(u)

    while S:
        v = S[-1]
        if t_in[v] == 0:
            time += 1
            t_in[v] = time
        # print(f'v: {v}')
        # print(f'S: {S}')

        s_first = len(S)
        for i in e[v]:  # 現在の vertex u に接続するもののうち値の大きい方からスタックする
            if fp[i - 1] is False:
                S.append(i - 1)
                fp[i - 1] = True

        if len(S) == s_first:
            time += 1
            S.pop()
            t_out[v] = time


while 0 in t_in:
    dfs(t_in.index(0))


for i in range(n):
    print(f'{i + 1} {t_in[i]} {t_out[i]}')
