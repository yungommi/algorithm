#예상 시간복잡도 O(N) 

import sys
input = sys.stdin.readline
N=int(input())

l = list(map(int,input().split()))
m = max(l)
s= sum(l)
print(100 * s / (N*m))
