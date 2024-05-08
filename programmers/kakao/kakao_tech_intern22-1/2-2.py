def solution(queue1, queue2):
    count = 0 
    sum_1 = sum(queue1)
    target = (sum_1 + sum(queue2)) // 2
    queue_0 = queue1 + queue2 
    i = 0
    j = len(queue1) -1
    while sum_1 != target and j<len(queue_0)-1:
        if sum_1 < target:
            j += 1
            sum_1 += queue_0[j]
            count +=1
        else:
            sum_1 -= queue_0[i]
            i +=1
            count +=1 
    if sum_1 == target:
        return count 
    else:
        return -1