# ALDS_5_A - 総当たり　
import sys

n = int(input())
A = list(map(int, sys.stdin.readline().strip().split()))
q = int(input())
m = list(map(int, sys.stdin.readline().strip().split()))

sum_set = set()

for i in range(2 ** n):
    bit = [(i >> j) & 1 for j in range(n)]
    combined = [x * y for (x, y) in zip(A, bit)]
    sum_set.add(sum(combined))

for target in m:
    if target in sum_set:
        print('yes')
    else:
        print('no')
