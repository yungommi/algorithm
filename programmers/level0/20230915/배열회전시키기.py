# 예상 시간복잡도: O(n)

def solution(numbers, direction):
    answer=[]
    if direction == 'right':
        answer.append(numbers[-1])
        answer += numbers[0:-1]
    else:
        answer += numbers[1:]
        answer.append(numbers[0])
        
    return answer

