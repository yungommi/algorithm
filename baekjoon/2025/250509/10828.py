#예상시간복잡도 : O(N)
import sys
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    tmp = list(input().split())
    if tmp[0]=='push':
        l.append(int(tmp[1]))
    elif tmp[0]=='top':
        if l:
            print(l[-1])
        else:
            print(-1)
    elif tmp[0]=='size':
        print(len(l))
    elif tmp[0]=='empty':
        if l:
            print(0)
        else:
            print(1)
    else:
        if l:
            x = l.pop()
            print(x)
        else:
            print(-1)


