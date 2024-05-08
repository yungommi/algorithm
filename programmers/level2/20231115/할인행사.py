# 예상 시간 복잡도 O(n) n:len(discount)  

def solution(want, number, discount):
    answer = 0
    new = []
    for i in range(len(want)):
        new += [want[i]] * number[i]
    new.sort()
    for i in range(0, len(discount)-9):
        tmp = discount[i:i+10]
        tmp.sort()
        if new == tmp:
            answer += 1
    return answer
