import sys
input = sys.stdin.readline 

a,b = map(int, input().split())

if a==b:
    print("same")
elif a>b:
    print("A")
else:
    print("B")