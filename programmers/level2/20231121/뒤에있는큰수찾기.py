# 예상 시간 복잡도 O(n^2)

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for idx, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            answer[stack.pop()] = number
        stack.append(idx)

    return answer

