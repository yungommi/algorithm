#예상 시간복잡도 O(log n * m ) 

import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
s = list(set(l))
s.sort()
dict = {}
for k in l:
    if k in dict:
        dict[k]+=1
    else:
        dict[k] = 1 

m = int(input())
ll = list(map(int,input().split()))
#0~~n-1
def func(k):
    st = 0 
    end = len(s)-1
    while st <= end:
        tmp = (st + end )//2
        if s[tmp]==k:
            return dict[k]
        elif s[tmp] > k :
            end = tmp-1
        else:
            st = tmp+1
    return 0

for i in ll:
    print(func(i), end=' ')

