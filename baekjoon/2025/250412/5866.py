#예상시간복잡도 : O(N)
import sys
input = sys.stdin.readline

B,E = map(int, input().split())
B_ = []
E_ = []
b_m, e_m = 0,0 
for _ in range (B):
    n,d = input().split()
    b_m += int(n) 
    if d == 'R':
        B_.append((int(n),1))
    else:
        B_.append((int(n),-1))
for _ in range (E):
    n,d = input().split()
    e_m += int(n) 
    if d == 'R':
        E_.append((int(n),1))
    else:
        E_.append((int(n),-1))

b_p = [0]*(b_m+1)
e_p = [0]*(e_m+1) 

cnt = 0 
for n,d in B_:
    for i in range(n):
        b_p[cnt+1] = b_p[cnt]+d 
        cnt+=1 
cnt = 0 
for n,d in E_:
    for i in range(n):
        e_p[cnt+1] = e_p[cnt]+d 
        cnt += 1

if e_m>b_m:
    for i in range(e_m - b_m):
        b_p.append(b_p[b_m])
elif e_m<b_m:
    for i in range(b_m-e_m):
        e_p.append(e_p[e_m])
n = max(e_m, b_m) 
flag = 1
ans = 0 
for i in range(1,n+1):
    if e_p[i]==b_p[i]:
        if flag == 0 :
            ans += 1 
            flag = 1 
    else:
        flag = 0 

print(ans)
