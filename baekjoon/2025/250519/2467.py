#예상시간복잡도 : O(n)
import sys
input = sys.stdin.readline

n = int(input())
sol = list(map(int, input().split()))
st = 0 
end = n-1 
ans = abs(sol[end]+sol[0])
x = 0
y = n-1 

while st<end:
    tmp = sol[st]+sol[end]
    #print(st, end, tmp, ans)
    if abs(tmp) <= ans:
        x = st
        y = end 
        ans = abs(tmp) 
        #print("changed", x,y,ans)
    if tmp == 0:
        #print(sol[x], sol[y])
        break 
    elif tmp>0:
        end -= 1 
    else:
        st += 1 
print(sol[x], sol[y])
    