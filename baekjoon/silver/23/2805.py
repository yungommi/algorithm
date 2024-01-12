# https://www.acmicpc.net/problem/2805

import sys
input = sys.stdin.readline

n,x = map(int, input().split())
trees =list(map(int, input().split()))

start = 1
end = max(trees)

while start <= end:
    mid = (start + end)// 2
    get = 0
    for itm in trees:
        get += max(itm - mid , 0)
        if get >= x:
            break
    if get >= x:
        start = mid+1 
    else :
        end = mid-1
  
print (end)
        
        


