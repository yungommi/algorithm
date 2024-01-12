# 예상 시간복잡도: O(n^2)

def solution(my_string, is_prefix):
    if my_string.find(is_prefix) == 0 :
        return 1
    else:
        return 0
    
