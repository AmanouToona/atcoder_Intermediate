# AtCoder Beginner Contest 014 C - AtColor
import sys

N = int(input())

cusum = [0] * (10 ** 6 + 2)
for n in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    cusum[a] += 1
    cusum[b + 1] -= 1

for n in range(10 ** 6 + 1):
    cusum[n + 1] += cusum[n]

print(max(cusum))


