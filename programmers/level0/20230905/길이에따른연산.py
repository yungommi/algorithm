# 예상 시간복잡도: O(n)

def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        mult = 1
        for i in num_list:
            mult *= i
        return mult
    

