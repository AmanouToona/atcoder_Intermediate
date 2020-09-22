# AtCoder Beginner Contest 034 C - 経路
import sys
from math import factorial

mod = 10 ** 9 + 7
w, h = map(int, sys.stdin.readline().strip().split())

H = max(w, h)
W = min(w, h)
# (W + H　- 2) C (W - 1) を求めるだけの問題
ans = 1
# まず分母を求める % mod 
for i in range(H, W + H - 1):
    ans *= i
    ans %= mod

# 逆元を用いて割っていく
ans = ans * pow(factorial(W - 1), mod-2, mod)
print(ans % mod)
