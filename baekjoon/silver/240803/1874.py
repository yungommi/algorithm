import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

stack =  []
ans = []
cur = 1

for i in range(n):
    new = int(input())
    while not(cur > new):
        stack.append(cur)
        cur += 1
        ans.append('+')
        
    if stack[-1] != new:
        ans = ['NO']
        break
    else:
        stack.pop()
        ans.append('-')        
        
for x in ans:
    print(x)
        


        

