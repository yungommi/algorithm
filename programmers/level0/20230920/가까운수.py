# 예상 시간복잡도: O(n)

def solution(array, n):
    array.sort(reverse=True)
    answer = 0
    l = []
    a = {}
    #print(min(list(map(lambda x: abs(x-n), array))))
    l = list(map(lambda x: abs(n-x), array))
    a = dict(zip(l, array))
    answer = a[min(a)]
    return answer

