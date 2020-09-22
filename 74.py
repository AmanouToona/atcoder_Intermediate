# AtCoder Beginner Contest 021 D - 多重ループ
import sys
from math import factorial

mod = 10 ** 9 + 7

n = int(input())
k = int(input())

ans = factorial(n + k - 1) % mod
ans = ans * pow(factorial(k), mod - 2, mod)
ans = ans * pow(factorial(n - 1), mod - 2, mod)

print(ans % mod)

