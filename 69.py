# AtCoder Beginner Contest 084 D - 2017-like Number
import sys

end_no = 10 ** 5

# 素数判定 エラストテネスの篩
def eratosthenes(N):
    prime = []  # 最後に素数一覧を返す
    data = [i for i in range(2, N + 1)]

    while True:
        p = data[0]

        if p >= N ** 0.5:
            return prime + data

        prime.append(p)
        data = [i for i in data[:] if i % p != 0]


prime = eratosthenes(end_no)
prime = set(prime)

# 累積和の用意
cusum = [0] * (end_no + 1)
for n in range(1, end_no + 1):
    cusum[n] = cusum[n - 1]
    if n % 2 == 0:
        continue

    if n in prime and int((n + 1) / 2) in prime:
        cusum[n] += 1


# 入力
Q = int(input())

for _ in range(Q):
    l, r = map(int ,sys.stdin.readline().strip().split())
    print(cusum[r] - cusum[l - 1])
