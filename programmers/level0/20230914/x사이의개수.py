# 예상 시간복잡도: O(n)

def solution(myString):
    answer = []
    tmp = myString.split("x")
    for x in tmp:
        answer.append(len(x))
    return answer

