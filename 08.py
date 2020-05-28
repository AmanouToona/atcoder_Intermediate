# Square869120Contest #6 B - AtCoder Markets

"""
無数に答えはあるが、入り口、出口の存在する位置を品物の位置に合わせて全探索すればよい
"""
import sys

N = int(input())

A, B, D = [], [], []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    A.append(a)
    B.append(b)
    D.append(b - a)


sum_D = sum(D)  # これは一定値

ans = float('inf')
for start in A:
    for goal in B:
        if start > goal:
            continue

        distance = sum_D
        for a, b in zip(A, B):
            distance += abs(a - start) + abs(b - goal)

        ans = min(ans, distance)

print(ans)
