# JOI 2008 予選 5 - おせんべい
import sys

R, C = map(int, sys.stdin.readline().strip().split())
state = []
for _ in range(R):
    state.append(list(map(int, sys.stdin.readline().strip().split())))
bit = [0] * R


def dfs(r=0):
    state[r] = [x for x in state[r]]
    dfs(r + 1)

    state[r] = [x != 1 for x in state[r]]


