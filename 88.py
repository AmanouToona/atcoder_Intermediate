# A - 碁石ならべ
import sys

n = int(input())  # 1 <= <= 10 ** 6

# color 0: white  1: black
board = [0]  # 色の変わった地点の数字を入れる  0 0 1　1 0 だったら、[0, 2, 4] となる
last_color = -1  # 最初は何も入っていない

for i in range(n):
    i += 1
    color = int(sys.stdin.readline().strip())

    if last_color != color:
        last_color = color

        if i % 2 == 1:
            board.append(i - 1)
        else:
            if len(board) == 1:
                continue
            else:
                board.pop()

# print(board)

u = n
u_color = last_color
white_tot = 0
while board:
    v = board.pop()
    if u_color == 0:
        white_tot += u - v
        u = v
        u_color = 1
    else:
        u = v
        u_color = 0

print(white_tot)
