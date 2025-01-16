import sys
input = sys.stdin.readline 

n = int(input())

l = list(map(int,input().split()))

d = [(l[i]-l[i-1]) for i in range(1,n)]

print(d.count(min(d)))