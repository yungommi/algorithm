# 예상 시간복잡도: O(ab) a: row b:column 

def solution(picture, k):
    answer = []
    for r in picture:
        tmp = ""
        for c in r:
            tmp += c*k
        for i in range(k):
            answer.append(tmp)
    return answer

