# JOI 2013 予選 4 - 暑い日々

import sys

# 配る DP で解いてみる

D, N = map(int, sys.stdin.readline().strip().split())
T = []  # temperature
for _ in range(D):
    T.append(int(input()))

A, B, C = [], [], []
for n in range(N):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    A.append(a)
    B.append(b)
    C.append(c)

# ---------------------------------
dp = [[-1] * N for _ in range(D)]
for n in range(N):
    if (A[n] > T[0]) or (B[n] < T[0]):
        continue
    dp[0][n] = 0


for d in range(D):
    for n in range(N):
        if dp[d][n] == -1:
            continue

        for nn in range(N):
            if (A[nn] > T[d + 1]) or (B[nn] < T[d + 1]):
                continue

            dp[d + 1][nn] = max(dp[d + 1][nn], dp[d][n] + abs(C[n] - C[nn]))

for i in range(len(dp)):
    print(dp[i])

print(max(dp[-1]))

