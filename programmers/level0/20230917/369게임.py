# 예상 시간복잡도 : O(n) n : order length

def solution(order):
    answer = 0
    for x in str(order):
        if x=='3' or x=='6'or x=='9':
            answer += 1
    return answer


