# NTL_1_B - べき乗
import sys 
mod = 10 ** 9 + 7

m, n = map(int, sys.stdin.readline().strip().split())

print(pow(m, n, mod))
