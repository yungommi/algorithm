# 예상 시간복잡도: O(N)

def solution(x):
    add = 0 
    for k in str(x):
        add += int(k)
    return x%add == 0 

