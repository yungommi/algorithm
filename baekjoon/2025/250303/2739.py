#예상 시간복잡도 O(1)

import sys
input = sys.stdin.readline

N = int(input())

for i in range(1,10):
    print(f"{N} * {i} = {N*i}")

