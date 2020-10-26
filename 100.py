# Tenka1 Programmer Beginner Contest D - Crossing
import sys

N = int(input())

# if N <= 2:
#     print('No')
#     sys.exit()

group = 1
while True:
    if N == group * (group + 1) / 2:
        break
    if group * (group + 1) / 2 >= N:
        print('No')
        sys.exit()
    group += 1


ans = [[] for _ in range(group + 1)]

count = 1
for i in range(group):
    for j in range(0, i + 1):
        if j != i:
            ans[j].append(count)
        else:
            ans[-1].append(count)
        ans[i].append(count)
        count += 1

print('Yes')
print(len(ans))
for a in ans:
    print(f'{group} {" ".join(map(str, a))}')
