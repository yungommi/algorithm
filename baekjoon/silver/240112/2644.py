'''https://www.acmicpc.net/problem/2644'''

import sys
input = sys.stdin.readline

n = int(input())
a,b = map(int, input().split())
i = int(input())
grp = {}

for _ in range(i):
    x,y = map(int, input().split())
    if x in grp:
        grp[x].append(y)
    else:
        grp[x]=[y]
    if y in grp:
        grp[y].append(x)
    else:
        grp[y]=[x]

def main(a,b,grp):
    l1 = [a]
    l2 = []
    done = [a]
    ans = 0
    while l1:
        ans += 1
        for k in l1:
            for j in grp[k]:
                if j==b:
                    return ans
                if j not in done:
                    l2.append(j)
                    done.append(j)
        l1 = l2
        l2 = []
    return -1 

print(main(a,b,grp))
