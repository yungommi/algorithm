# 예상 시간복잡도: O(n)

def solution(num_list):
    answer = [0,0]
    for x in num_list:
        if x %2 == 1:
            answer[1] += 1
        else:
            answer [0] += 1
    return answer
