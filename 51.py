# 51 JOI 2014 予選 4 - 部活のスケジュール表

# 列に出席者のbit 行に n日目をとる
# 配るdp

import sys
sys.setrecursionlimit(10 ** 8)

mod = 10007

N = int(input())
I = list(sys.stdin.readline())
I = I[:-1]
member = ['I',  'O', 'J']

# dp 初期化
# bit: J, O, I　とする。例えばJ君のみ出席ならば、100 とする。
dp = [[0] * (2 ** 3) for _ in range(N)]
for i in range(2 ** 3):
    if (i >> 2) & 1 == 1:  # J 君が出席している
        if (i >> member.index(I[0])) & 1 == 1:  # 責任者が出席している
            dp[0][i] = 1


# dp 解く
for n in range(N - 1):  # n日目の出席者から n+1 日目の出席可能者を記入
    for i in range(2 ** 3):
        if dp[n][i] == 0:
            continue

        for j in range(2 ** 3):  # n + 1日目の出席者
            if i & j != 0:  # n + 1 日目に n日目と同じ出席者が存在する
                if (j >> member.index(I[n + 1])) & 1 == 1:
                    dp[n + 1][j] += dp[n][i]


ans = sum(dp[-1]) % mod
print(ans)
