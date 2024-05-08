# 예상 시간복잡도: O(N)

def solution(n):
    n= str(n)
    ans = []
    for i in n :
        ans.append(int(i))
    ans.reverse()
    return ans

