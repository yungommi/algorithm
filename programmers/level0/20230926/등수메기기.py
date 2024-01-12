# 예상 시간복잡도: O(n)

def solution(score):
    ans = []
    li = []
    for i in score:
        li.append(sum(i))
    sort_arr = sorted(li,reverse=True)
    for i in li:
        ans.append(sort_arr.index(i)+1)
        
    return ans

