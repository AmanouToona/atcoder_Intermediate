# AOJ 1167 - ポロック予想
# 配るDP でいってみよ～

import sys


def main():
    tetra_nums = [i * (i + 1) * (i + 2) // 6 for i in range(1, 181)]
    N = 10 ** 6

    dp = [i for i in range(N)]
    dp_odd = [i for i in range(N)]

    for n in range(N):
        for tetra_num in tetra_nums:
            next_n = n + tetra_num

            if next_n < N:
                next_dp = dp[n] + 1
                if next_dp < dp[next_n]:
                    dp[next_n] = next_dp

                if tetra_num & 1:
                    next_dp = dp_odd[n] + 1
                    if next_dp < dp_odd[next_n]:
                        dp_odd[next_n] = next_dp

    while True:
        num = int(sys.stdin.readline())
        if num == 0:
            break
        print(dp[num], dp_odd[num])


if __name__ == '__main__':
    main()

