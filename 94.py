# AOJ 1149 - ケーキカット
import sys

while True:
    n, w, d = map(int, sys.stdin.readline().strip().split())

    if n == 0 and w == 0 and d == 0:
        break

    cake = [(w, d)]
    for _ in range(n):
        p, s = map(int, sys.stdin.readline().strip().split())
        # print(f'cake {cake}, p: {p - 1}, s: {s}')
        p -= 1

        u_w, u_d = cake[p]
        s %= (u_w + u_d)

        if s < u_w:
            cake.append((min(u_w - s, s), u_d))
            cake.append((max(u_w - s, s), u_d))
        else:
            s -= u_w
            cake.append((u_w, min(u_d - s, s)))
            cake.append((u_w, max(u_d - s, s)))
        cake.pop(p)

    cake = [w * d for w, d in cake]
    cake.sort()
    print(' '.join(map(str, cake)))
