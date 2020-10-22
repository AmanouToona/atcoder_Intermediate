# AtCoder Beginner Contest 149 B - Greedy Takahashi　
import sys

A, B, K = map(int, sys.stdin.readline().strip().split())

if A >= K:
    print(A - K, B)
else:
    print(0, max(B - K + A, 0))
