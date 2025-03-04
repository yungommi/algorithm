#예상시간복잡도 : O(N)
import sys 
input = sys.stdin.readline 

N,R,C = map(int, input().split())

size = 2 ** N 
ans = 0

while size > 1:
    size = size // 2 
    if R < size and C < size:
        pass 
    elif R < size and C >= size : #2사분
        ans += size ** 2
        C -= size 
    elif R >= size and C < size: #3사분 
        ans += size**2 *2 
        R -= size 
    else: #4사분 
        ans += size**2 *3 
        C -= size 
        R -= size
print(ans) 

'''
시간초과 : O(4^N)

import sys 
input = sys.stdin.readline 

N,R,C = map(int, input().split())

idx = 2*(R%2) + C%2
std = (R-R%2 , C-C%2)

mul = 2 
tmp0 = [(0,0)]
while True:
    if std in tmp0:
        break
    tmp1 = []
    tmp2 = []
    tmp3 = []
    for itm in tmp0:
        x,y = itm 
        tmp1.append((x,y+mul))
        tmp2.append((x+mul,y))
        tmp3.append((x+mul,y+mul))
    mul *= 2 
    tmp0 += tmp1
    tmp0 += tmp2
    tmp0 += tmp3 
    
#print(tmp0)
#print(tmp0.index(std))
stdidx = tmp0.index(std)
print(stdidx * 4 + idx)
'''