# DDCC2020 予選 D - Digit Sum Replace

import sys

M = int(input())
total_d = 0
total_c = 0
for m in range(M):
    d, c = map(int, sys.stdin.readline().strip().split())
    total_d += d * c
    total_c += c

# if total_d >= 10:
#     ans = total_c + total_d // 9 - 1
# else:
#     ans = total_c - 1

ans = total_c - 1

if total_d >= 10:
    ans += total_d // 9

    if total_d % 9 == 0:
        ans -= 1

print(ans)
