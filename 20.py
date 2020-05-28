# AtCoder Beginner Contest 077 C - Snuke Festival　

import sys

N = int(input())
A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))
C = list(map(int, sys.stdin.readline().strip().split()))

A = sorted(A)
B = sorted(B)
C = sorted(C)


def search(i, S):  # i : search する数値  S: search対象の数列　　大きいものの個数を返す
    if S[0] > i:
        return len(S)
    if S[-1] <= i:
        return 0

    left = 0
    right = len(S) - 1

    while right - left != 1:
        # print(f'right:{right}, left:{left}')
        mid = int((left + right) / 2)
        if S[mid] <= i:
            left = mid
        else:
            right = mid

    return len(S) - (left + 1)


def search1(i, S):  # i : search する数値  S: search対象の数列  小さいものの個数を返す
    if S[0] >= i:
        return 0
    if S[-1] < i:
        return len(S)

    left = 0  # 満たす
    right = len(S) - 1  # 満たさない

    while right - left != 1:
        mid = int((left + right) / 2)
        if S[mid] < i:
            left = mid
        else:
            right = mid

    return left + 1


ans = 0
for b in B:
    ans_a = search1(b, A)
    ans_c = search(b, C)

    ans += ans_a * ans_c

print(ans)
