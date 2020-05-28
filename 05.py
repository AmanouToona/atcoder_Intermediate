# AtCoder Beginner Contest 095 C - Half and Half
import sys

A, B, C, X, Y = map(int, sys.stdin.readline().strip().split())

"""
ans = A * X + B * Y
for z in range(2, 2 * 10 ** 5 + 1, 2):
    x = max(X - int(z / 2), 0)
    y = max(Y - int(z / 2), 0)

    price = A * x + B * y + C * z
    ans = min(price, ans)

print(ans)
"""

price1 = A * X + B * Y
price2 = C * 2 * X + B * max(Y - X, 0)
price3 = A * max(X - Y, 0) + C * 2 * Y
print(min(price1, price2, price3))

