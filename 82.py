# AOJ 2013 - 大崎
import sys


def time2sec(S):
    S = S.split(":")

    sec = 0
    sec += (int(str(S[0])[0]) * 10  + int(str(S[0])[1])) * 3600  # 1 hour = 3600 sec
    sec += (int(str(S[1])[0]) * 10  + int(str(S[1])[1])) * 60  # 1 min = 60 sec
    sec += (int(str(S[2])[0]) * 10  + int(str(S[2])[1])) * 1  # 1sec = 1 sec

    return sec


def main():
    while True:
        cusum = [0] * (24 * 3600 + 1) 

        N = int(input())  # <= 10 ** 4
        if N == 0:
            break

        for n in range(N):
            s1, s2 = map(str, sys.stdin.readline().strip().split())

            cusum[time2sec(s1)] += 1
            cusum[time2sec(s2)] -= 1
        
        for i in range(24 * 3600):
            cusum[i + 1] += cusum[i]
        
        print(max(cusum))



if __name__ == '__main__':
    main()
