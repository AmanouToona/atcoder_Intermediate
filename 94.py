# AOJ 1149 - ケーキカット
import sys

n, w, d = map(int, sys.stdin.readline().strip().split())

cake = [(w * d, w, d)]
for _ in range(n):
    p, s = map(int, sys.stdin.readline().strip().split())
    cake.sort(key=lambda x: x[0])


