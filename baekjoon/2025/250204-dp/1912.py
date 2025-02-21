#예상 시간복잡도 O(n) 

import sys
input = sys.stdin.readline

n = int(input())
ll = list(map(int, input().split()))

for i in range(1,n):
    ll[i] = max(ll[i], ll[i]+ll[i-1])

print(max(ll))