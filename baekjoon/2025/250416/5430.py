#예상시간복잡도 : O(T*(N+P))
import sys
input = sys.stdin.readline 
from collections import deque 

T = int(input())

def function(p,l):
    arr = deque(l)
    flip = False 
    for x in p:
        if x =='R':
            flip = not flip 
        else:
            if not arr:
                return 'error'
            elif flip:
                arr.pop()
            else:
                arr.popleft() 
    if flip:
        arr.reverse()
    return ('['+','.join(map(str,arr))+']')


for i in range(T):
    p = [x for x in input().rstrip()]
    n = int(input())
    inp = input().rstrip()
    if n>0:
        inp = inp[1:-1]
        inp = list(map(int,inp.split(',')))
        print(function(p,inp))
    else:
        print(function(p,[]))