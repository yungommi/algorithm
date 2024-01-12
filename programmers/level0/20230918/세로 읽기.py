# 예상 시간 복잡도 : O(n) 


def solution(my_string, m, c):
    answer = [my_string[i] for i in range(c-1,len(my_string),m)]
    return ''.join(answer)


