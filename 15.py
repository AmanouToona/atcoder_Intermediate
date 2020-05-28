# AtCoder Beginner Contest 145 C - Average Length

import sys
import numpy as np
import itertools

N = int(input())
town = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    town.append((x, y))


def distance(i, j):
    ans = np.sqrt((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2)
    return ans


total = 0
for i in itertools.permutations(iterable=town):
    for j in range(len(i) - 1):
        total += distance(i[j], i[j + 1])

n_fact = 1
for i in range(1, N + 1):
    n_fact *= i

ans = total / n_fact

print(ans)
