# AtCoder Beginner Contest 144 D - Water Bottle

import sys
import math

a, b, x = map(int, sys.stdin.readline().strip().split())

if x <= a ** 2 * b * 0.5:
    ans = math.atan(a * b ** 2 / (2 * x))
else:
    ans = math.atan(2 * (a ** 2 * b - x) / a ** 3)

print(math.degrees(ans))
