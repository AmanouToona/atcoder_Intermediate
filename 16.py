# AtCoder Beginner Contest 150 C - Count Order

import sys
import itertools

N = int(input())

P = list(map(int, sys.stdin.readline().strip().split()))
Q = list(map(int, sys.stdin.readline().strip().split()))


count = 1
a, b = 0, 0
for i in itertools.permutations([i for i in range(1, N+1)]):
    i = list(i)
    if i == P:
        a = count
    if i == Q:
        b = count
    count += 1

print(abs(a - b))
