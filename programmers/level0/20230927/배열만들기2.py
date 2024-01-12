# 예상 시간복잡도: O(n)

def solution(l,r):
    ans = []
    for i in range(l,r+1):
        if all(num in ['0','5'] for num in str(i)):
            ans.append(i)
    if ans:
        return ans
    else:
        return [-1]
    
