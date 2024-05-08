# 예상 시간복잡도: O(N)

def solution(left, right):
    ans = 0
    for x in range(left, right+1):
        ans += get(x)
    return ans

def get(n):
    ans = 0
    for i in range(1,n+1):
        if n%i == 0:
            ans += 1 
    if ans % 2 == 0 :
        return n
    else:
        return -n
    
    