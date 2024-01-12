# 예상 시간복잡도: O(n)

def solution(num_list):
    answer = 0
    for x in num_list:
        while x >1:
            if x%2 == 1:
                x = (x-1)/2
            else:
                x = x/2
            answer += 1
    return answer

