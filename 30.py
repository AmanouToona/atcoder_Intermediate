# JOI 2011 予選 5 - チーズ
import sys
import heapq
import copy
# copy が滅茶苦茶遅い。　copy を使わない実装でないとまず通らない


def bfs(start, end, state, time=0):
    global H, W
    # print(f'start: {start}, end: {end}')
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (time, start))
    xu, yu = start[0], start[1]
    state[yu][xu] = 'X'

    xe, ye = end[0], end[1]

    while q:
        # print(f'q: {q}, ', end='')
        time, u = heapq.heappop(q)
        # print(f'time: {time}')
        xu, yu = u[0], u[1]

        if (xu == xe) and (yu == ye):
            break

        for i in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            xv = xu + i[0]
            yv = yu + i[1]
            if (xv < 0) or (xv >= W):
                continue
            if (yv < 0) or (yv >= H):
                continue
            if state[yv][xv] == 'X':
                continue
            heapq.heappush(q, (time + 1, (xv, yv)))
            state[yv][xv] = 'X'

    return time


def main():
    global H, W
    H, W, N = map(int, sys.stdin.readline().strip().split())

    # s: 巣,  x: 障害物, .:空地, 1 ~ 9: 硬さ
    M = []  # Map
    turn = dict()  # 探索する地点を記録する
    for h in range(H):
        m = list(map(str, sys.stdin.readline()))
        M.append(m)
        for w, j in enumerate(m):
            if (j is not '.') and (j is not 'X'):
                turn[j] = (w, h)
    # 方針: ある地点からある地点までの最短経路を求めるプログラムを作成して、s, 1, 2, ... 9 と繰り返せばよい


    time = 0
    for i in range(N):
        # print(f'ans time: {time}')
        # print(M)
        state = copy.deepcopy(M)
        if i == 0:
            time = bfs(turn['S'], turn[str(i + 1)], state, time=time)
        else:
            time = bfs(turn[str(i)], turn[str(i + 1)], state, time=time)

    print(time)


if __name__=='__main__':
    main()

