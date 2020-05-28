# AtCoder Regular Contest 054 B - ムーアの法則
import math

P = float(input())

optim_x = 1.5 * math.log2(P * math.log(2) / 1.5)
# print(optim_x)

# opt1 = max(0, math.floor(optim_x))
# opt2 = max(0, math.ceil(optim_x))

opt1 = max(0, optim_x)
opt2 = max(0, optim_x)


ans1 = opt1 + P / (2 ** (opt1 / 1.5))
ans2 = opt2 + P / (2 ** (opt2 / 1.5))

print(min(ans1, ans2))
