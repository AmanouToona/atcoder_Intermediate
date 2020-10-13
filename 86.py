# AtCoder Beginner Contest 075 C - Bridge
"""
union find を使った解法
"""

import sys

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents =  [-1] * n  # 負値 :-size  正:parent を表す
    
    def find(self, x):  # root を返す
        if self.parents[x] < 0:
            return x
        else:
            return self.find(self.parents[x])
    
    def union(self, x, y):  # x, y を結合する
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return
        
        if self.parents[x_root] > self.parents[y_root]:
            x_root, y_root = y_root, x_root

        self.parents[x_root] += self.parents[y_root]
        self.parents[y_root] = x_root            

    def size(self, x):  # x が含まれる木のサイズを返す
        return - self.parents[self.find(x)]
    
    def same(self, x, y):  # x, y が同一の木に含まれるか返す
        return self.find(x) == self.find(y)
    
    def members(self, x):  # x を含む木に含まれるメンバーをかえす
        x_root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == x_root]
    
    def roots(self):   # 根の一覧を返す
        return [i for i in range(self.n) if self.parents[i] < 0]


N, M = map(int, sys.stdin.readline().strip().split())

unionfind = UnionFind(N)
edge = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    a -= 1
    b -= 1
    
    edge.append((a, b))

bridge = 0
for m in range(M):
    unionfind = UnionFind(N)
    for m2 in range(M):
        if m2 == m:
            continue
        a, b = edge[m2]

        unionfind.union(a, b)
    
    a, b = edge[m]
    if not unionfind.same(a, b):
        bridge += 1

print(bridge)




