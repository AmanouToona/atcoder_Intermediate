# 三井住友信託銀行プログラミングコンテスト 2019 D - Lucky PIN

import sys

N = int(input())
S = input()

ans = 0
for i in range(10):
    code1 = S.find(str(i))
    if code1 == -1:
        continue
    for j in range(10):
        code2 = S.find(str(j), code1 + 1)
        if code2 == -1:
            continue
        for k in range(10):
            if S.find(str(k), code2 + 1) != -1:
                ans += 1

print(ans)
