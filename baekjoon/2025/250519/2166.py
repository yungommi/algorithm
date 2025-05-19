#예상시간복잡도 : O(n)
import sys
input = sys.stdin.readline

n = int(input())
x = [0]*(n+1)
y = [0]*(n+1)

for i in range(n):
    a,b = map(int, input().split())
    x[i]=a
    y[i]=b 
x[n]=x[0]
y[n]=y[0]

i = 0
j = 1
ans = 0
while j<=n:
    ans += x[i]*y[j]
    ans -= x[j]*y[i]
    i += 1 
    j += 1 
ans = 0.5 * abs(ans)
print(ans)