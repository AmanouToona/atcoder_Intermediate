# Square869120Contest #3 B - 石落としゲーム

import sys
import copy

"""
4 4 2
3413
4121
1424
2312
"""

H, W, K = map(int, sys.stdin.readline().strip().split())

if K >= 4:
    print(0)
    sys.exit()

C = []
for h in range(H):
    c = str(input())
    c = [int(i) for i in list(c)]
    C.append(c)


def search(row, i):
    score = 0
    left = 0
    right = left + 1

    while True:
        if row[left] == row[right]:
            right += 1
            if right < W:
                continue

        if right - left >= K:
            score += 2 ** i * (right - left) * row[left]
            row[left: right] = [0] * (right - left)

        left = right

        if right == W:
            break

    return score


def fall(board):
    for w in range(W):
        upper = H - 1

        # for row in board:
        #     print(row)
        # print()

        for h_under in range(H - 1, -1, -1):
            # print(f'h_under: {h_under}, w: {w}')
            if board[h_under][w] == 0:
                under = h_under
                upper = min(under - 1, upper)

                for h_upper in range(upper, -1, -1):
                    if board[h_upper][w] != 0:
                        upper = h_upper

                        board[under][w] = board[upper][w]
                        board[upper][w] = 0
                        upper -= 1
                        break

    return


ans_score = 0
for w in range(W):
    for h in range(H):
        board = copy.deepcopy(C)

        board[h][w] = 0

        total_score = 0
        i = 0
        while True:
            fall(board)

            score = 0
            for h in range(H):
                score += search(board[h], i)
            if score == 0:
                break

            i += 1
            total_score += score

        ans_score = max(ans_score, total_score)

print(ans_score)
