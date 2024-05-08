# 예상 시간복잡도: O(n)

def solution(cipher, code):
    answer = ''
    for i in range(code-1, len(cipher), code):
        answer += cipher[i]
    return answer

