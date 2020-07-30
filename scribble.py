V = 4
S = (1 << V) - 1
S = S ^ (1 << 0)

print(format(S, 'b'))

print(format(S ^ (1 << 0), 'b'))



