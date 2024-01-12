# 예상 시간복잡도: O(N)

def solution(phone_number):
    l = len(phone_number)
    return '*'*(l-4)+phone_number[l-4:]

