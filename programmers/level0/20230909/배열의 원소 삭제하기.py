# 예상 시간복잡도: O(n)

def solution(arr, delete_list):
    answer = []
    for x in arr:
        if x in delete_list:
            pass
        else:
            answer.append(x)
    return answer
