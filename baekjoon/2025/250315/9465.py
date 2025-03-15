#예상시간복잡도 : O(N)

import sys
input = sys.stdin.readline

def function(N):
    if N==1:
        l0 = int(input())
        l1 = int(input())
        return max(l0,l1)
    l0 = list(map(int,input().split()))
    l1 = list(map(int,input().split()))
    l0[1] = l1[0]+l0[1]
    l1[1] = l0[0]+l1[1]
    for i in range(2,N):
        l0[i] = max(l1[i-1]+l0[i], l1[i-2]+l0[i])
        l1[i] = max(l0[i-1]+l1[i], l0[i-2]+l1[i])
    return max(l0[N-1], l1[N-1])


i = int(input())
for _ in range(i):
    N= int(input())
    print(function(N))
