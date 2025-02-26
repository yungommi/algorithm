#예상 시간복잡도 O(1) 

import sys
input = sys.stdin.readline
A,B,C = map(int,input().split())

if (C-B)%(A-B) == 0 : 
    print((C-B)//(A-B))
else:
    print((C-B)//(A-B)+1)

