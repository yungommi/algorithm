# 예상 시간복잡도: O(n)

def solution(A, B):
    for i in range(len(A)):
        tmp = A[len(A)-i:] + A[:len(A)-i]
        if tmp == B:
            return i
    return -1
