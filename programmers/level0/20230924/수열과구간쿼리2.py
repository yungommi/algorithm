# 예상 시간복잡도: O(n)

def solution(arr, queries):
    result = []
    for q in queries:
        tmp = []
        for i in range(q[0], q[1] + 1):
            if arr[i] > q[2]:
                tmp.append(arr[i])
        try:   
            result.append(min(tmp))
        except:
            result.append(-1)
    return result

