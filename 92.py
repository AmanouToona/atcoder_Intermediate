# AOJ 1193 - 連鎖消滅パズル
import sys

"""
5
5 9 5 5 9
5 5 6 9 9
4 6 3 6 9
3 3 2 9 9
2 2 1 1 1
"""
while True:
    H = int(sys.stdin.readline().strip())  # 1 <= H <= 10

    if H == 0:
        break

    board = []
    for h in range(H):
        row = list(map(int, sys.stdin.readline().strip().split()))
        board.append(row)


    def search(row):
        for start in [0, 1, 2]:
            continuous = 1
            for end in range(start + 1, 5):
                if row[start] == 0:
                    continue

                if row[start] == row[end]:
                    continuous += 1
                else:
                    break
            if continuous >= 3:
                score = row[start] * continuous
                row[start: start + continuous] = [0] * continuous
                return continuous, score
        return continuous, 0


    score = 0
    while True:
        # 石の削除
        end = True
        for h in range(H):
            row = board[h]

            continuous, row_score = search(row)
            if continuous >= 3:
                end = False
                score += row_score
        if end:
            break

        # for h in board:
        #     print(h)
        # print()

        # 石の落下
        for w in range(5):
            # print(f'w: {w}')
            top = H - 1
            while top >= 1:
                # print(f'top: {top}, {board[top][w]}')
                if board[top][w] != 0:
                    top -= 1
                    continue

                for ceiling in range(top - 1, -1, -1):
                    # print(f'ceiling {ceiling}')
                    if board[ceiling][w] == 0:
                        continue

                    board[top][w] = board[ceiling][w]
                    board[ceiling][w] = 0
                    break

                top -= 1

        # print('stone fall')
        # for h in board:
        #     print(h)
        # print(score)
        # print()

    print(score)
