import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
d = deque()

for i in range(n):
    new = input().split()
    if new[0]=='push':
        d.append(int(new[1]))
    elif new[0]=='pop':
        if d:
            tmp = d.popleft()
            print(tmp)
        else:
            print(-1)
    elif new[0]=='size':
        print(len(d))
    elif new[0]=='empty':
        if d:
            print(0)
        else:
            print(1)
    elif new[0]=='front':
        if d:
            print(d[0])
        else:
            print(-1)
    elif new[0]=='back':
        if d:
            print(d[-1])
        else:
            print(-1)
