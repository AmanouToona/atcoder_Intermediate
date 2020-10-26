# AtCoder Beginner Contest 150 D - Semi Common Multiple
import sys
import math


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm_list(A):
    lcm = A[0]
    for a in A[1:]:
        lcm = lcm_base(lcm, a)
    
    return lcm


# input 
N, M = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))


p = 0
t = A[0]
while t % 2 == 0:
    p += 1
    t //= 2

for a in A[:]:
    q = 0
    while a % 2 == 0:
        q += 1
        a //= 2
    if q != p:
        print(0)
        sys.exit()

first_half_lcm = lcm_list(A) // 2

if first_half_lcm > M:
    print(0)
elif first_half_lcm in A:
    print(0)
else:
    ans = 1 + (M - first_half_lcm) // lcm_list(A)
    print(ans)
