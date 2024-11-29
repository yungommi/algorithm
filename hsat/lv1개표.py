import sys
input=sys.stdin.readline 

def function(x):
    quo, rem = divmod(x,5)
    return ('++++ '*quo + '|'*rem)

n = int(input())
for _ in range(n):
    print(function(int(input())))