import sys
input = sys.stdin.readline

l= []
n = int(input())
for i in range(n):
    inp = list(map(int, input().split('.')))
    l.append(inp)
    
l.sort()

for x in l:
    print('.'.join(str(k) for k in x))