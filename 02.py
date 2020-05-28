# 02 AtCoder Beginner Contest 106 B - 105
import sys
import math

N = int(input())


def divisor(n):
    ans = 0
    for i in range(1, int(math.sqrt(n + 1)), 2):  # 偶数は回答に含めないため、約数が　2の倍数となる数字は存在しない
        if n % i == 0:
            ans += 1
            if i != int(math.sqrt(n + 1)):
                ans += 1

    return ans


ans = 0
for i in range(105, N + 1, 2):  # 偶数は回答に含めない
    if divisor(i) == 8:
        ans +=1

print(ans)
