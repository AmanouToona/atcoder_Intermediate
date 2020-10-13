# A - 鉄道旅行 (Railroad Trip) 
import sys

# 入力 ------------------
N, M = map(int, sys.stdin.readline().strip().split())
P = list(map(int, sys.stdin.readline().strip().split()))  # 長さ M

A = [0] * (N - 1)
B = [0] * (N - 1)
C = [0] * (N - 1)

for n in range(N - 1):
    a, b, c = map(int, sys.stdin.readline().strip().split())

    A[n] = a
    B[n] = b
    C[n] = c

cusum = [0] * N
for m in range(M - 1):
    cusum[min(P[m], P[m + 1]) - 1] += 1
    cusum[max(P[m], P[m + 1]) - 1] -= 1

for n in range(N - 1):
    cusum[n + 1] += cusum[n]


cost = 0
for n in range(N - 1):
    cost += min(A[n] * cusum[n], B[n] * cusum[n] + C[n])

print(cost)
