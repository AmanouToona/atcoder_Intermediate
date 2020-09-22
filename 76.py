# 全国統一プログラミング王決定戦本戦 A - Abundant Resources
import sys

N = int(input())
A = list(map(int, sys.stdin.readline().strip().split()))

cusum = [0]
for a in A:
    tail = cusum[-1]
    cusum.append(tail + a)

for i in range(1, N + 1):
    left = 0
    right = left + i

    ans = 0

    while right <= N:
        ans = max(ans, cusum[right] - cusum[left])

        left += 1
        right += 1

    print(ans)
