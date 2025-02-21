#예상 시간복잡도 O(n^2) 

import sys
input = sys.stdin.readline
n = int(input())

def func(n):
    room = [1]*(n+1)
    room[0]=0
    for i in range(2,n+1):
        tmp = i
        while tmp <= n:
            if room[tmp]==0:
                room[tmp]=1
            else:
                room[tmp]=0
            tmp += i 
    return sum(room)

for k in range(n):
    m = int(input())
    print(func(m))