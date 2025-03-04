#예상시간복잡도 : O(N)

import sys 
input = sys.stdin.readline 

while True :
    l = list(map(int, input().split()))
    l.sort()
    a,b,c=l[0],l[1],l[2]
    if c == 0:
        break
    else:
        if c**2 == a**2 + b**2:
            print('right')
        else:
            print('wrong')

