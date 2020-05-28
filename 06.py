# 三井住友信託銀行プログラミングコンテスト 2019 D - Lucky PIN

import sys


def main():
    N = int(input())  # 桁数
    S = str(input())

    ans = set()

    digit1 = set()

    for i in range(0, N - 2):
        if S[i] in digit1:
            continue
        digit1.add(S[i])
        digit2 = set()

        for j in range(i + 1, N - 1):
            if S[j] in digit2:
                continue
            digit2.add(S[j])
            digit3 = set()
            for k in range(j + 1, N):
                if len(digit3) == 10:
                    break
                code = S[i] + S[j] + S[k]
                ans.add(code)

    print(len(ans))


if __name__ == '__main__':
    main()
