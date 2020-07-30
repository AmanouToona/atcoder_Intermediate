# DPL_2_A - 巡回セールスマン問題
# dp の与え方を変えた

import sys
sys.setrecursionlimit(10 ** 8)

V, E = map(int, sys.stdin.readline().strip().split())
d = [[float('inf')] * V for _ in range(V)]
for _ in range(E):
    s, t, _d = map(int, sys.stdin.readline().strip().split())
    d[s][t] = _d

# dp 初期化 -----------------
dp = [[float('inf')] * V for _ in range(1 << V)]  # 1 << V は 2 ** V に同じ
dp[0][0] = 0  # 頂点 0 からスタートするとする


def res(s, v):
    # s: すでに訪問した街の集合, v: 今いる街の集合, dp: 動的計画法のテーブル
    # 0 から出発して s, v　を満たすコストを返す関数

    if dp[s][v] == -1:  # 到達不可能ならば
        return float('inf')
    elif dp[s][v] != float('inf'):
        return dp[s][v]
    elif (s >> v) & 1 == 0:  # 集合 s に頂点 v が含まれていないならば
        dp[s][v] = -1
        return float('inf')

    ans = float('inf')
    for u in range(V):
        # if (s >> u) & 1 == 1:  # ここで止めてしまうと解答が得られない
        # print(f's: {format(s ^ (1 << v), "b")}, u: {u}')
        # print(f'{d[u][v]}')
        ans = min(ans, res(s ^ (1 << v), u) + d[u][v])

    if ans == float('inf'):  # 到達不可能ならば　
        dp[s][v] = -1
    else:
        dp[s][v] = ans

    return ans


res((1 << V) - 1, 0)

# for i in range(len(dp)):
#     print(dp[i])
print(dp[-1][0])

