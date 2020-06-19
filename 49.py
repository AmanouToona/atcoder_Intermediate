# DPL_2_A - 巡回セールスマン問題

import sys
sys.setrecursionlimit(10 ** 8)


V, E = map(int, sys.stdin.readline().strip().split())
d = [[float('inf')] * V for _ in range(V)]
for _ in range(E):
    s, t, _d = map(int, sys.stdin.readline().strip().split())
    d[s][t] = _d

# dp 初期化 -----------------
dp = [[float('inf')] * V for _ in range(1 << V)]  # 1 << V は 2 ** V に同じ


def res(s, v, dp):
    # s: すでに訪問した街の集合, v: 今いる街の集合, dp: 動的計画法のテーブル
    # s, v, dp を満たしているときに、すべての街を訪問して 0 に戻るコストを返す関数

    if (s == (1 << V) - 1) and (v == 0):
        dp[s][v] = 0
        return 0
    if dp[s][v] == -1:  # たどり着けないことが保証されているとき。　TLE防止。
        return float('inf')
    if dp[s][v] != float('inf'):
        return dp[s][v]

    ans = float('inf')
    for u in range(V):
        # if (1 << u) & s == 0:
        if (s >> u & 1) == 0:  # 町 u　に訪問していない
            ans = min(res(s | (1 << u), u, dp) + d[v][u], ans)

    if ans == float('inf'):  # TLE 防止。  探索してたどり着けないことが保証されるときは -1 を入れる
        dp[s][v] = -1
    else:
        dp[s][v] = ans
    return ans


ans = res(0, 0, dp)
if ans == float('inf'):
    print(-1)
else:
    print(ans)
