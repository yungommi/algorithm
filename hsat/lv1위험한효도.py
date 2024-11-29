import sys
input = sys.stdin.readline 

a,b,m = map(int,input().split())
ans = 0

quo, res = divmod(m,a)

if res ==0:
    ans += quo * (a + b) -b
else:
    ans += quo * (a + b) + res

quo, res = divmod(m,b)

if res ==0:
    ans += quo * (a + b) -b
else:
    ans += quo * (a + b) + res

print(ans)