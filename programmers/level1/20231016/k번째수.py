# 예상 시간복잡도: O(N)

def solution(array, commands):
    answer = []
    for x in commands:
        i=x[0]-1
        j=x[1]
        n=x[2]-1
        tmp = array[i:j]
        tmp.sort()
        answer.append(tmp[n])
    return answer

