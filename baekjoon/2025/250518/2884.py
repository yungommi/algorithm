#예상시간복잡도 : O(1)
import sys
input = sys.stdin.readline

a,b = map(int, input().split())
time = a*60 + b - 45 
if time<0 :
    time += 60*24
print(time//60, time%60)

