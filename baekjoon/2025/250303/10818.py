#예상 시간복잡도  : O(1)

import sys 
input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))

print(min(l), end = ' ')
print(max(l))
