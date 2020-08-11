import sys
import bisect

N = int(input())

ans = 0
dp = [float('inf')] * N

for n in range(N):
    now = int(input())
    point = bisect.bisect_right(dp, now)

    if dp[point] != float('inf'):
        ans += 1

    dp[point] = now

print(ans)
