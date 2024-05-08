# 예상 시간복잡도: O(N)

def solution(answers):
    answer = []
    l = len(answers)
    a1 = [1,2,3,4,5] * (l-1)
    a2 = [ 2, 1, 2, 3, 2, 4, 2, 5] *(l-1)
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*(l-1)
    aa = [0,0,0]
    for i in range(l):
        if a1[i]== answers[i]:
            aa[0]+= 1
        if a2[i]== answers[i]:
            aa[1]+= 1
        if a3[i]== answers[i]:
            aa[2]+= 1
    m = max(aa)
    for i in range(3):
        if aa[i] ==m :
            answer.append(i+1)
    return answer

