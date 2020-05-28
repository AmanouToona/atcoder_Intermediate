# AtCoder Beginner Contest 122 B - ATCoder
import sys

S = str(input())
target = ['A', 'C', 'G', 'T']

ans = 0
temp_ans = 0
for s in S:
    if s in target:
        temp_ans += 1
    else:
        temp_ans = 0
    ans = max(ans, temp_ans)

print(ans)
