import sys
input = sys.stdin.readline

n = int(input())
ll = []
for _ in range(n):
    a,b = map(int,input().split())
    ll.append((a,b))

ll.sort(key=lambda x:x[1])

a,b = ll[0]
print(a, b)
