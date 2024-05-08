# 예상 시간복잡도: O(n^2)

def solution(my_strings, parts):
    answer = ""
    for i in range(len(my_strings)):
        tmp = my_strings[i]
        s = int(parts[i][0])
        e = int(parts[i][1]+1)
        answer += tmp[s:e]
    return answer

