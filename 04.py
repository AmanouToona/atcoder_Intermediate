# パ研杯2019 C - カラオケ
import sys

N, M = map(int, sys.stdin.readline().strip().split())
A = []
for n in range(N):
    A.append(list(map(int, sys.stdin.readline().strip().split())))


def calc_score(t1, t2, A):
    score = 0
    for n in range(N):
        score += max(A[n][t1], A[n][t2])
    return score


max_score = 0
for t1 in range(M-1):
    for t2 in range(t1 + 1, M):
        score = calc_score(t1, t2, A)
        max_score = max(max_score, score)

print(max_score)
