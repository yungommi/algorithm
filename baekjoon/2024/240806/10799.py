#예상 시간 복잡도 O(n) 

import sys
input = sys.stdin.readline

inp = str(input())

stack = 0 
count = 0 
for i in range(0, len(inp)):
    if inp[i]=='(':
        if inp[i+1]==')':
            count += stack 
        else:
            stack += 1 
            count += 1
    else:
        if inp[i-1]=='(':
            pass
        else:
            stack -= 1 

print(count)
