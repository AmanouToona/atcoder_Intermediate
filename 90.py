# Square869120Contest #5 B - Emblem
import sys

N, M = map(int, sys.stdin.readline().strip().split())  # 0 <= N, M <= 100, N + M >= 2

r_min = float('inf')
fixed_circle = []
# 最小の半径を記録しつつ入力を受ける
for n in range(N):
    # -100 <= x, y <= 100,  1<= r <= 100
    x, y, r = map(int, sys.stdin.readline().strip().split())
    fixed_circle.append((x, y, r))
    r_min = min(r_min, r)

free_circle = []
center_constraint = None
for m in range(M):
    x, y = map(int, sys.stdin.readline().strip().split())

    for fixed_x, fixed_y, fixed_r in fixed_circle:
        r = ((fixed_x - x) ** 2 + (fixed_y - y) ** 2) ** 0.5 - fixed_r

        r_min = min(r_min, r)

    for free_x, free_y in free_circle:
        r = ((free_x - x) ** 2 + (free_y - y) ** 2) ** 0.5 / 2

        r_min = min(r_min, r)

    free_circle.append((x, y))

print(r_min)
