'''https://www.acmicpc.net/problem/1012'''

import sys
input = sys.stdin.readline
from collections import deque 

def main(w,h,num):
    cab = [0]*num
    for i in range(num):
        x,y = map(int, input().split())
        cab[i] = (x,y)
    done = []
    ans = 0
    done = set()
    while cab:
        new = cab.pop()
        q = deque()
        q.append(new)
        ans += 1
        while q:
            tmp = q.popleft()
            for itm in cab:
                if itm[0]==tmp[0] and abs(itm[1]-tmp[1])==1:
                    q.append(itm)
                    done.add(itm)
                elif itm[1]==tmp[1] and abs(itm[0]-tmp[0])==1:
                    q.append(itm)
                    done.add(itm)
            cab = list(set(cab) - done)
    return ans

n = int(input())
for _ in range(n):
    w,h,num = map(int, input().split())
    print(main(w,h,num))
