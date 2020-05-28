# ALDS_5_A - 総当たり

import sys

n = int(input())
A = list(map(int, sys.stdin.readline().strip().split()))
q = int(input())
m = list(map(int, sys.stdin.readline().strip().split()))


def dfs(index, target, actual_state):
    if target == actual_state:
        return True

    if actual_state > target:
        return False
    if sum(A[index:]) < target - actual_state:
        return False

    return dfs(index+1, target, actual_state) or dfs(index+1, target, actual_state+A[index])


for target in m:
    if dfs(0, target, 0):
        print('yes')
    else:
        print('no')
