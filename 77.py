# JOI 2010 本選 1 - 旅人
import sys

mod = 10 ** 5

# 入力
n, m = map(int, sys.stdin.readline().strip().split())

dist = []
for _ in range(n - 1):
    dist.append(int(input()))

A = []
for _ in range(m):
    A.append(int(input()))

# 累積和の計算
cusum = [0] * n
for i, d in enumerate(dist):
    cusum[i + 1] = cusum[i] + d
    cusum[i + 1] %= mod

# 答えの計算
ans = 0
u = 0
for a in A:
    v = u + a
    _left = min(u, v)
    _right = max(u, v)
    ans += cusum[_right] - cusum[_left]
    ans %= mod
    u = v

print(ans % mod)
