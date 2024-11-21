#예상 시간복잡도 O(Nlog(max(ll))) 

import sys
input = sys.stdin.readline

n = int(input())
ll = list(map(int, input().split()))
money = int(input())

ll.sort() 
st = 0 
end = ll[-1]

while st<=end:
    mid = (st + end)//2 
    add = 0 
    for x in ll:
        if x<= mid: 
            add += x 
        else:
            add += mid
    if add > money:
        end = mid -1 
    else:
        st = mid + 1 
        answer = mid

print(answer)
