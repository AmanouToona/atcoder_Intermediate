# E - Colorful Hats 2
import sys

mod = 1000000007

N = int(input())
A = list(map(int, sys.stdin.readline().strip().split()))

hat = [0] * 3

ans = 1
for a in A:
    ans *= hat.count(a)
    ans %= mod
    if ans == 0:
        print(ans)
        sys.exit()
    hat[hat.index(a)] += 1

print(ans)
