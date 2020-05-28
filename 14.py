# Square869120Contest #4 B - Buildings are Colorful!　
# 分割統治法 ver
import sys

N, K = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))


def dfs(height=a[0], cost=0, target=K, can_see=1, i=1):
    if can_see >= target:
        # print('height', height)
        # print('can_see', can_see)
        # print('cost', cost)
        return cost

    # 端まで探索したとき
    if i == len(a):
        return float('inf')

    # 建物 i を選ばない場合
    if height >= a[i]:
        cost1 = dfs(height=height, cost=cost, target=K, can_see=can_see, i=i+1)
    else:
        cost1 = dfs(height=a[i], cost=cost, target=K, can_see=can_see+1, i=i+1)
    # print('cost1', cost1, 'can_see', can_see, 'i', i)

    # 建物　i を選んだ場合
    cost += max(0, height + 1 - a[i])
    height = max(a[i], height + 1)
    cost2 = dfs(height=height, cost=cost, target=K, can_see=can_see+1, i=i+1)
    # print('cost2', cost2)

    return min(cost1, cost2)


print(dfs(a[0], cost=0, target=K, can_see=1, i=1))

