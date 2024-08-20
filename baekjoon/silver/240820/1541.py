#예상 시간복잡도 O(n) 

import sys
import re 

input = sys.stdin.readline

inp = str(input())

list = re.findall(r'\d+|[+-]', inp)

ans = 0 
ope = 1 
for x in list:
    if x == '+':
        pass
    elif x == '-':
        ope = -1
    else:
        ans += ope * int(x)

print(ans)

#  '\d+  :   하나 이상의 숫자 
#  |  :  or
#  [+-]  :  '+', '-' 