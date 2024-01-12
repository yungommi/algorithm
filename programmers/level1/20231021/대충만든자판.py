# 예상 시간복잡도: O(N)

def solution(keymap, targets):
    d = {}
    for x in keymap:
        for i in range(len(x)):
            if x[i] in d:
                d[x[i]] = min(d[x[i]], i+1)
            else:
                d[x[i]]=i+1
    print(d)
    answer = [0]*len(targets)
    for x in range(len(targets)):
        for k in targets[x]:
            if k not in d:
                answer[x] = -1
                break
            else:
                answer[x] += d[k]
    return answer

