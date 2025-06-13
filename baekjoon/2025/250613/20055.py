#예상시간복잡도 : O(max(A)*N^2)
import sys
input = sys.stdin.readline
from collections import deque 

n,k = map(int, input().split())

l = list(map(int, input().split()))
field = deque(l) 

step = 0 
robot = deque([False for i in range(n)])

while True: 
    #1
    step += 1 
    field.rotate(1)
    robot.rotate(1)
    robot[-1]=False 
    #2 
    for i in range(n-2, -1, -1):
        if robot[i] and not robot[i+1] and field[i+1]>=1:
            robot[i+1]=True
            robot[i]=False
            field[i+1] -= 1 
    robot[-1]=False 
    #3 
    if field[0]>0:
        robot[0]=True 
        field[0] -= 1 
    #4 
    if field.count(0)>=k: 
        break

print(step)
