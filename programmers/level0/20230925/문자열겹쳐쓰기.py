# 예상 시간복잡도: O(n)

def solution(my_string, overwrite_string, s):
    l_ = len(overwrite_string)
    answer = my_string[:s] + overwrite_string + my_string[s+l_:]
    return answer

