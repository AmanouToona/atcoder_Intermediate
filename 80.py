# GigaCode 2019 D - 家の建設
import sys

# 入力
H, W, K, V = map(int, sys.stdin.readline().strip().split())
# H: height W: width K: 建築コスト V: 所持金

cusum = []
cusum.append([0] * (W + 1))
for _ in range(H):
    A = list(map(int, sys.stdin.readline().strip().split()))
    A = [0] + A
    cusum.append(A)

# 累積和を取る
for h in range(H):
    for w in range(W):
        cusum[h + 1][w + 1] += cusum[h + 1][w] + cusum[h][w + 1] - cusum[h][w]

ans = 0
for h in range(1, H + 1):
    for w in range(1, W + 1):
        if h * w * K > V:  # 建設費用のみで所持額を超える
            break
        if h * w <= ans:  # すでに購入可能だとわかっている土地以下の大きさならば確かめる必要がない
            break

        for h_ul in range(1, H + 1 - (h - 1), h):  # h upper left
            for w_ul in range(1, W + 1 - (w - 1), w):  # w upper left
                h_lr = h_ul + h - 1  # h lower right
                w_lr = w_ul + w - 1  # w lower right
                land_price = cusum[h_lr][w_lr] - cusum[h_lr][w_ul - 1] - cusum[h_ul - 1][w_lr - 1] + cusum[h_ul - 1][w_ul - 1]

                if land_price + K * (h * w) <= V:
                    ans = h * w
                    break
            else:
                continue
            break

print(ans)

