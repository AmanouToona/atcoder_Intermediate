# AtCoder Beginner Contest 023 D - 射撃王
import sys

N = int(input())  # 10 **5
H = []  # 10 ** 9
S = []
for n in range(N):
    h, s = map(int, sys.stdin.readline().strip().split())
    H.append(h)
    S.append(s)


# #  高度　h までに風船を割り切れるか判断する関数
def judge(H, S, target_h):
    limit = [(target_h - h) // s for h, s in zip(H, S)]  # 何秒以内に割ればよいかを算出する
    limit = sorted(limit)  # 余裕の少ないものを優先する
    # print(f'target_h: {target_h}')
    # print(f'limit : {limit}')
    for i, j in enumerate(limit):
        if j < i:  # 割らないといけない秒数よりも時間がかかるならば失敗
            return False
    return True


ok = 10 ** 6 * (10 ** 10) + 10 ** 9
ng = 0
while ok - ng > 1:
    mid = (ok + ng) // 2
    if judge(H, S, mid):
        ok = mid
    else:
        ng = mid
    # print(f'ok: {ok}, ng: {ng}')

print(ok)

