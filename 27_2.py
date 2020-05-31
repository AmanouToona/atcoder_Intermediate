# JOI 2009 予選 4 - 薄氷渡り　

import sys
sys.setrecursionlimit(10 ** 9)

M = int(input())
N = int(input())

FP = []
for n in range(N):
    G = list(map(int, sys.stdin.readline().strip().split()))
    G = [True if g == 1 else False for g in G]
    FP.extend(G)


def dfs(u, fp, counter):
    # fp: footprint: 探索可能であるか記録する
    # return: max depth, x(max depth), y(max_depth)

    x, y = u[0], u[1]
    FP[x + y * M] = False

    fp[x + y * M] = False
    counter += 1
    x_ans, y_ans = x, y
    count_ans = counter

    for i in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        x_next = x + i[0]
        y_next = y + i[1]
        if (x_next < 0) or (x_next >= M):
            continue
        if (y_next < 0) or (y_next >= N):
            continue
        if fp[x_next + y_next * M]:
            x_temp, y_temp, count_temp = dfs((x_next, y_next), fp, counter)
            if count_temp > count_ans:
                x_ans, y_ans, count_ans = x_temp, y_temp, count_temp

    fp[x + y * M] = True
    return x_ans, y_ans, count_ans


fp = FP.copy()
fp2 = FP.copy()
ans = 0
while True in FP:
    u = FP.index(True)
    y = int(u // M)
    x = int(u - y * M)

    x_temp, y_temp, count_temp = dfs((x, y), fp, 0)  # 一度　 dfs で最も氷を割れる経路を探索する
    # print(x_temp, y_temp, count_temp)

    _, _, ans_temp = dfs((x_temp, y_temp), fp2, 0)  # 最も氷を割れた経路の終着点から、最も氷を割れる経路を探索する
    # やってることのイメージは木の直径を求めることに近い。　最も遠い点と最も遠い点の間の距離を求める
    ans = max(ans, ans_temp)

    # print(f'x_ans: {x_ans}, y_ans: {y_ans}, count_ans: {count_ans}')

print(ans)
