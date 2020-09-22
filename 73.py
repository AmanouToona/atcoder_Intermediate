# AtCoder Beginner Contest 145 D - Knight
import sys
from math import factorial

mod = 10 ** 9 + 7

X, Y = map(int, sys.stdin.readline().strip().split())

# 合計の移動回数は Total = X + Y / 3 
# 移動方法は A: (i + 1, j + 2)  B: (i + 2, j + 1) の2通り
# 移動回数は A: 2 * Total - X  B: X - Total 

# 到達不可能であるか判断する
if (X + Y) % 3 != 0:
    print(0)
    sys.exit()

if Y > 2 * X or Y < X * 0.5:
    print(0)
    sys.exit()


Total = (X + Y) // 3
A = Total * 2 - X
B = X - Total

# combination の計算
ans = 1
for i in range(1, Total + 1):
    ans *= i
    ans %= mod

ans = ans * pow(factorial(A), mod - 2, mod)
ans = ans * pow(factorial(B), mod - 2, mod)

print(ans % mod)

