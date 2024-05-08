# 예상 시간복잡도: O(n)

def solution(num_list):
    a,b = 1,0
    for x in num_list:
        a *= x
        b += x
    if a < b**2 :
        return 1
    else:
        return 0 

