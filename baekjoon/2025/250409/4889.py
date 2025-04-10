#예상시간복잡도 : O(N^2)

import sys
input = sys.stdin.readline
from collections import deque

def function(st):
    ans = 0
    stack = [] 
    st = deque(list(st))
    while st:
        tmp = st.popleft()
        if tmp == '}':
            if stack and stack[-1]=='{':
                stack.pop()
            else:
                ans += 1 
                stack.append('{')
        else:
            stack.append(tmp)
    return str(ans + len(stack)//2)
n = 1
while True:    
    inp = input().rstrip()
    if '-' in inp:
        break
    else:
        res = function(inp)
        print(str(n)+'. '+res)
        n+= 1
        