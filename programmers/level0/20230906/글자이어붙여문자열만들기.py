# 예상 시간복잡도: O(n)

def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer += my_string[int(i)]
    return answer

