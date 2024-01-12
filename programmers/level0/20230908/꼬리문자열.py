# 예상 시간복잡도: O(nk)

def solution(str_list, ex):
    answer = ''
    for x in str_list:
        if ex in x:
            pass
        else:
            answer += x
    return answer

