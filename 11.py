# AtCoder Beginner Contest 128 C - Switches

import sys

N, M = map(int, sys.stdin.readline().strip().split())

S = [[0] * N for _ in range(M)]  # 電球に関連するスイッチを1, 関連しないスイッチを0 として状態を保持
for i in range(M):
    _, *s = map(int, sys.stdin.readline().strip().split())
    for j in s:
        S[i][j-1] = 1  # 電球i に関連するスイッチj の状態S[i][j - 1]　を1にする
p = list(map(int, sys.stdin.readline().strip().split()))

ans = 0
for i in range(2 ** N):
    bit = [(i >> j) & 1 for j in range(N)]  # スイッチの状態を表すビット列を作成
    for i, s in enumerate(S):
        o_e = sum([x * y for x, y in zip(s, bit)]) % 2  # 点灯条件を導出
        if o_e != p[i]:  # 点灯条件に当てはまらないならば次の条件の探索に移る
            break
    else:  # 点灯条件に当てはまるならば、回答に 1 を足す
        ans += 1

print(ans)
