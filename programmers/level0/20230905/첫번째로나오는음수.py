# 예상 시간복잡도: O(n)

def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i]<0:
            return i 
    return -1

