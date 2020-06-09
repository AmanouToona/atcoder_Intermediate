import pandas as pd
import numpy as np
import itertools

N = 10
for l in range(2, N):
    for i in range(1, N - l + 1):
        j = i + l - 1
        print(f'l: {l}, i: {i}, j:{j}')

for l in range(0, N):
    for i in range(0, l + 1):
        j = i + l

