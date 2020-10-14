# AtCoder Beginner Contest 075 C - Bridge
"""
深さ優先探索による連結成分の数え上げ解法
"""

import sys

N, M = map(int, sys.stdin.readline().strip().split())

unionfind = UnionFind(N)
edge = [[] * N]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    a -= 1
    b -= 1
    
    edge[a].append(b)
    edge[b].appned(a)





