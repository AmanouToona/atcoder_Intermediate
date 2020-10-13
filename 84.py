# JOI 2012 本選 4 - 釘
import sys

"""
5 2
2 2 1
2 1 3
"""

N, M = map(int, sys.stdin.readline().strip().split())  # 2 <= N <= 5000, 1 <= M <= 5 * 10 ** 5


cusum = [[0] * (i + 1) for i in range(1, N + 3)]
for m in range(M):
    a, b, x = map(int, sys.stdin.readline().strip().split())

    # 0 index に変換
    a -= 1
    b -= 1

    # 三角形の上頂点
    cusum[a][b] += 1
    cusum[a][b + 1] -= 1

    # 三角形の左頂点
    cusum[a + x + 1][b] -= 1
    cusum[a + x + 2][b + 1] += 1

    # 三角形の右頂点
    cusum[a + x + 1][b + x + 2] += 1
    cusum[a + x + 2][b + x + 2] -= 1


# imos法による累積和の取得
# 横方向　左から右へ
for h in range(0, N + 2):
    for w in range(0, h + 1):
        cusum[h][w + 1] += cusum[h][w]

# 斜め方向　右上から左下へ
for h in range(0, N + 1):
    for w in range(0, h + 1):
        cusum[h + 1][w] += cusum[h][w]

# 斜め方向　左上から右下へ
for h in range(0, N + 1):
    for w in range(0, h + 1):
        cusum[h + 1][w + 1] += cusum[h][w]



ans = 0
for row in cusum:
    for element in row:
        if element != 0:
            ans += 1

print(ans)
