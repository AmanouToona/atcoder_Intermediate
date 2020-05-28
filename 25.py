import sys
sys.setrecursionlimit(10 ** 9)

first = True
while True:
    W, H = map(int, sys.stdin.readline().strip().split())
    if (W == 0) and (H == 0):
        break

    fp = [True] * (W * H)  # 探索可能示す

    M = []
    for h in range(H):
        m = list(map(int, sys.stdin.readline().strip().split()))
        M.append(m)
        for i, j in enumerate(m):
            if j == 0:
                fp[h * W + i] = False


    def dfs(u):  # u は座標
        x, y = u
        fp[y * W + x] = False  # 探索済みを示す

        for i in [-1, 0, 1]:
            x_next = x + i
            if (x_next < 0) or (x_next > W - 1):
                continue
            for j in [-1, 0, 1]:
                y_next = y + j
                if (y_next < 0) or (y_next > H - 1):
                    continue
                # print(f'y_next: {y_next}, x_next: {x_next}')
                # print(f'{fp[y_next * W + x_next]}')
                # print(f'{M[y][x]}')
                if fp[y_next * W + x_next] and (M[y][x] == 1):
                    dfs((x_next, y_next))


    count = 0
    while True in fp:
        count += 1
        # print(f'count : {count}')
        # print(f'fp: {fp}')

        y = int((fp.index(True) / W))
        x = int((fp.index(True) - y * W))
        # print(f'x: {x}, y: {y}')
        dfs((x, y))

    # if first:
    #     first = False
    # else:
    #     print('\n', end='')
    print(count, end='\n')
