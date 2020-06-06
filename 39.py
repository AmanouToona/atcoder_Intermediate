# JOI 2011 予選 4 - 1 年生

import sys

N = int(input())
A = list(map(int, sys.stdin.readline().strip().split()))

# # 下のプログラムは A[0] = 0 で 2倍 の答えを返してしまう
# # dp 初期化
# dp = [[0] * 21 for _ in range(N)]  # 入力の内 N -1 個の数字で目的の数字を作るので range(N)
# dp[0][0] = 1  # 最初は何も数字を選んでいない状態が1通りあるのみ
#
# # ------------------------------------------------------------------------------------
# for i in range(N - 1):
#     a = A[i]
#     for j in range(21):
#         next_j1 = j + a
#         if next_j1 <= 20:
#             dp[i + 1][next_j1] += dp[i][j]
#
#         next_j2 = j - a
#         if next_j2 >= 0:
#             dp[i + 1][next_j2] += dp[i][j]
#
# for i in range(len(dp)):
#     print(dp[i])

# dp 初期化
dp = [[0] * 21 for _ in range(N - 1)]  # 入力の内 N-1 この数字で目的の数字を作る
dp[0][A[0]] = 1  # 最初は A[0] を選んだ 1通りのみが存在する

# ----------------------------------------------------------------------------------
for i, a in enumerate(A[1: -1]):
    for j in range(21):
        next_j1 = j + a
        if next_j1 <= 20:
            dp[i + 1][next_j1] += dp[i][j]

        next_j2 = j - a
        if next_j2 >= 0:
            dp[i + 1][next_j2] += dp[i][j]

# for i in range(len(dp)):
#     print(dp[i])

print(dp[-1][A[-1]])
