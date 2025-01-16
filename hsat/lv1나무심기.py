import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
l.sort()
print(max(l[0]*l[1], l[n-1]*l[n-2]))