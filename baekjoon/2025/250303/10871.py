#예상 시간복잡도 O(N)

import sys
input = sys.stdin.readline

N,X = map(int,input().split())
ll= list(map(int,input().split()))
for itm in ll:
    if itm<X:
        print(itm, end=' ')

