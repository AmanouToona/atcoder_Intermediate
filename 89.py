# JOI 2013 本選 1 - 電飾
import sys

N = int(input())  # 2 <= N <= 100_000
bulbs = list(map(int, sys.stdin.readline().strip().split()))

v_bulb = -1  # 一番最初は0, 1, ではない数値ならば何でもいい
continuous = [0, 0]  # 交互の点灯の記録が保たれている長さを保存するリスト
continuous_count = 0
for u_bulb in bulbs:

    if v_bulb != u_bulb:
        continuous_count += 1
    else:
        continuous.append(continuous_count)
        continuous_count = 1

    v_bulb = u_bulb
continuous.append(continuous_count)

# print(continuous)
# continuous の連続する3つの数値の和の最大値が回答となる
ans = 0
for i in range(N):
    ans = max(sum(continuous[i: i + 3]), ans)

print(ans)
