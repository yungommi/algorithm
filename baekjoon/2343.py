# https://www.acmicpc.net/problem/2343

import sys 
input = sys.stdin.readline 

n,m = map(int,input().split())
lec = list(map(int,input().split()))

start = 0
end = 10000 * m 
result = 10000 * m 

while start <= end :
    mid = (start + end) //2 
    used_n,length = 1,0
    print(start, mid, end)
    for itm in lec:
        if length + itm > mid:
            used_n += 1 
            length = itm
        else:
            length += itm 
    print(used_n)
    if used_n > m:
        start = mid+1
    else:
        end = mid - 1
        result = min(result , mid)
print(result)