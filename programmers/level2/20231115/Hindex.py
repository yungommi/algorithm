# 예상 시간 복잡도 O(n)

def solution(citations):
    answer = 0
    citations.sort()
    citations.reverse()
    i = 1
    while True:
        if citations[i-1] < i:
            return i-1
        elif i == len(citations):
            return i
        else:
            i += 1
            

