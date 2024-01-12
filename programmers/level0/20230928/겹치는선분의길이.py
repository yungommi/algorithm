# 예상 시간복잡도: O(ab)


def solution(lines):
    lines_ = []
    ans = []
    for line in lines:
        for i in range(line[0],line[1]):
            if i in lines_:
                ans.append(i)
            else:
                lines_.append(i)     
    return len(set(ans))

