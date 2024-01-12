# 예상 시간복잡도: O(n)

def solution(myString):
    answer = ''
    for x in myString:
        if x == 'a' or x == 'A':
            answer += "A"
        else:
            answer += x.lower()
    return answer

