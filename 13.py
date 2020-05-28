# JOI 2008 予選 5 - おせんべい
import sys
import numpy as np

R, C = map(int, sys.stdin.readline().strip().split())
state = []
for _ in range(R):
    state.append(list(map(int, sys.stdin.readline().strip().split())))
state = np.array(state)

ans = 0
for i in range(2 ** R):
    bit = np.array([(i >> j) & 1 for j in range(R)])
    bit = np.repeat(bit, C).reshape(R, C)
    ok = np.equal(state, bit).sum(axis=0)
    ng = R - ok

    count = np.maximum(ok, ng)
    ans = max(ans, count.sum())

print(ans)


# import numpy
# r,c=map(int,input().split())
# a=numpy.array([list(map(int,input().split())) for s in range(r)])
# ans=0
# for i in range(2**r):
#     bit=numpy.array([[i>>j&1] for j in range(r)])
#     black=numpy.sum(a^bit,axis=0)
#     ans=max(ans,sum(numpy.fmax(r-black,black)))
# print(ans)