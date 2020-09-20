# Square869120Contest #1 E - 散歩
import sys
mod = 10 ** 9 + 7

N, Q = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))
C = list(map(int, sys.stdin.readline().strip().split()))

# 移動ステップの累積和の導出
cusum = [0] * N  # 街は 0index
u = 0
for v in range(1, N):
    cusum[v] = cusum[u]
    cusum[v] += pow(A[u], A[v])

    u = v

# 答えの導出
steps = 0
u = 0
for v in C:
    v -= 1

    if cusum[v] >= cusum[u]:
        steps += cusum[v] - cusum[u]
    else:
        steps += cusum[u] - cusum[v]
    
    steps %= mod

    u = v

steps += abs(cusum[u] - cusum[0])

print(steps % mod)
