# ALDS_10_C - 最長共通部分列

import sys


# def main(): 
#     q = int(input())
#
#     for _ in range(q):
#         X = list(str(sys.stdin.readline().strip()))
#         Y = list(str(sys.stdin.readline().strip()))
#
#         dp = [[0] * (len(X) + 1) for _ in range(len(Y) + 1)]
#
#         for y in range(len(Y)):
#             for x in range(len(X)):
#                 dp[y + 1][x + 1] = max(dp[y][x + 1], dp[y + 1][x])
#                 if X[x] == Y[y]:
#                     dp[y + 1][x + 1] = dp[y][x] + 1
#
#         print(dp[-1][-1])


def main():
    q = int(input())

    for _ in range(q):
        X = list(str(sys.stdin.readline().strip()))
        Y = list(str(sys.stdin.readline().strip()))

        dp = [0] * (len(X) + 1)

        for y in range(len(Y)):
            dp2 = dp[:]
            for x in range(len(X)):
                if X[x] == Y[y]:
                    dp[x + 1] = dp2[x] + 1
                elif dp[x + 1] < dp[x]:
                    dp[x + 1] = dp[x]

        print(dp[-1])


if __name__ == '__main__':
    main()

