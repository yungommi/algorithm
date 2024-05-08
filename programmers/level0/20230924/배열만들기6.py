# 예상 시간복잡도: O(n)

def solution(arr):
    stk=[]
    i = 0
    while i<len(arr):
        if not(stk):
            stk.append(arr[i])
            i += 1 
        elif stk[-1]==arr[i]:
            stk.pop()
            i += 1 
        else:
            stk.append(arr[i])
            i += 1
    if stk:
        return stk
    else:
        return [-1]
    

