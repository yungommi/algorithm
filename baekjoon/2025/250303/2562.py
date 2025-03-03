# 예상 시간 복잡도  : O(1)

import sys
input = sys.stdin.readline

idx = 0 
max = 0 

for i in range(1,10):
    n = int(input())
    if n > max:
        idx = i 
        max = n 

print(max)
print(idx)

