# JOI 2012 予選 4 - パスタ

import sys

base = 10000

N, K = map(int, sys.stdin.readline().strip().split())

reservation = dict()
A, B = [], []
for k in range(K):
    a, b = map(int, sys.stdin.readline().strip().split())
    reservation[a] = b - 1  # パスタの種類は 0, 1, 2 とすると扱いやすい

# dp 初期化 -------------------------------
dp = [[0] * 3 for _ in range(N)]  # N日間 3種類
dp[0] = [1] * 3  # 1日目
if 1 in reservation.keys():
    for j in range(3):
        if j != reservation[1]:
            dp[0][j] = 0

for j in range(3):  # 2日目
    for jj in range(3):
        dp[1][jj] += dp[0][j]
if 2 in reservation.keys():
    for j in range(3):
        if j != reservation[2]:
            dp[1][j] = 0

# dp 計算 -------------------------------
for i in range(2, N):  # i + 1 日目
    for j in range(3):  # パスタの種類
        # print(f'i: {i} j: {j}')
        if dp[i - 1][j] != 0:
            dp[i][j] = sum(dp[i - 1]) + sum(dp[i - 2]) - (dp[i - 1][j] + dp[i - 2][j])
        else:
            dp[i][j] = sum(dp[i - 1])

    if i + 1 in reservation.keys():
        for j in range(3):
            if j != reservation[i + 1]:
                dp[i][j] = 0

# for i in range(len(dp)):
#     print(dp[i])

print(sum(dp[-1]) % base)


"""
解説
パスタの種類を a, b, c とする
ある日のパスタ x を食べる総予定数を x
その翌日のパスタ x を食べる総予定数を x'
その翌日のパスタ x を食べる総予定数を x'' とする


この時、例えばパスタaについて
a'' = a' + b' + c' - パスタa を3日連続で食べることになってしまう予定
が成り立つ。

3日連続で食べることになってしまう予定　とは ある日とその翌日にパスタa　を食べているので、
3日連続で食べることになってしまう予定　= a' - b - c がほぼ成り立つ
心は、 a' となる予定は ある日にパスタa　を食べていた a' を探すこと

"""



