#예상시간복잡도 : O(NlogN)
import sys
input = sys.stdin.readline

N = int(input())
l = [0]*N
for i in range(N):
    age, name = input().split()
    l[i] = [int(age),i,name]
l.sort() 
for a,i,n in l:
    print(a, n)
    