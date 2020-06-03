# ALDS_10_A - フィボナッチ数

n = int(input())

dp = [0] * (n + 1)

for i in range(n + 1):
    if (i == 0) or (i == 1):
        dp[i] = 1
    else:
        dp[i] = dp[i - 1] + dp[i - 2]

print(dp[-1])
# print(dp)
