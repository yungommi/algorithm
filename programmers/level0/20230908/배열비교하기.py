# 예상 시간복잡도: O(a+b)

def solution(arr1, arr2):
    l1 = len(arr1)
    l2 = len(arr2)
    if l1 == l2:
        if sum(arr1) > sum(arr2):   
            return 1
        elif sum(arr1) < sum(arr2): 
            return -1
        else:
            return 0 
    elif l1>l2:
            return 1
    else:
            return -1
