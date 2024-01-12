# 예상 시간복잡도: O(n)

def solution(my_string, indices):
    tmp = []
    for i in range(len(my_string)):
        if i in indices:
            pass
        else:
            tmp.append(my_string[i])
    return "".join(tmp)

