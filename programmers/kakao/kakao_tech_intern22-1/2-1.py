def solution(queue1, queue2):
    target = (sum(queue1) + sum(queue2)) // 2
    cur = sum(queue1)
    queue3 = queue1 + queue2 + queue1
    len1 = len(queue1)
    len2 = len(queue2)

    s = 0
    e = len1 - 1
    answer = 0
    while True:
        if cur == target:
            return answer
        if cur < target:
            e += 1
            if e >= len1 + len2 + len1:
                return -1
            cur += queue3[e]
        else:
            cur -= queue3[s]
            s += 1
        answer += 1