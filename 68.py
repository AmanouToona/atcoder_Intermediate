# NTL_1_A - 素因数分解　
import sys

n = int(input())
print(f'{n}:', end='')

ans = 2
while ans <= n ** 0.5:
    if n % ans == 0:
        print(f' {ans}', end='')
        n /= ans
    else:
        ans += 1

if n != 1:
    print(f' {int(n)}', end='')
print('')
