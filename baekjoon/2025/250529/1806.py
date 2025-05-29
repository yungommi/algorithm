#예상시간복잡도 : O(N))
import sys
input = sys.stdin.readline

N,S = map(int,input().split())
l = list(map(int, input().split()))
sum = 0 
left, right = 0,0 
ans = 1000000000 
while True:  
    if sum>=S:
        ans = min(ans, right-left)
        sum -= l[left]
        left += 1 
    elif right ==N:
        break
    else:
        sum += l[right]
        right += 1 

if ans == 1000000000:
    print(0)
else:
    print(ans) 