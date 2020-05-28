# ALDS_4_B - 二分探索

import sys

n = int(input())
S = list(map(int, sys.stdin.readline().strip().split()))
q = int(input())
T = list(map(int, sys.stdin.readline().strip().split()))


def search(i, S):  # i は探索対象 S : 探索する数列
    if S[0] > i:
        return False
    if S[-1] == i:
        return True

    left = 0
    right = len(S) - 1

    while right - left != 1:
        mid = int((left + right) / 2)
        if S[mid] <= i:
            left = mid
        else:
            right = mid

    if S[left] == i:
        return True
    else:
        return False


ans = 0
for t in T:
    if search(t, S):
        ans += 1

print(ans)
