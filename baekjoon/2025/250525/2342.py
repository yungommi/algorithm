#예상시간복잡도 : O(N^2+M)
import sys
input = sys.stdin.readline

inp = list(map(int,input().split()))
ans = 0 
st = inp[0]
for i in range(1,len(inp)-1):
    next = inp[i]
    if st == next:
        ans += 1 
    elif next == 0:
        ans += 2 
    elif abs(next-st)==1:
        ans += 3
    else:
        ans += 4
    st = next 
    #print(ans)
print(ans)