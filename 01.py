# ITP1_7_B - How Many Ways
import sys


def dfs(A, n, x):
    global ans
    if len(A) == 3:
        if sum(A) == x:
            ans += 1
        return

    else:
        if A:
            mini = max(A) + 1
        else:
            mini = 1

        for i in range(mini, n+1):
            B = A.copy()
            B.append(i)
            dfs(B, n, x)


while True:
    n, x = map(int, sys.stdin.readline().strip().split())
    if (n == 0) & (x == 0):
        break

    A = []
    ans = 0
    dfs(A, n, x)
    print(ans)



