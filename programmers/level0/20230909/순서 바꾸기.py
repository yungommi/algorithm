# 예상 시간복잡도: O(n)

def solution(num_list, n):
    answer = num_list[n:]+num_list[0:n]
    return answer

