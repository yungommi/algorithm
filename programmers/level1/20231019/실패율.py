# 예상 시간복잡도: O(N)

def solution(N, stages):
    n_stage = {}
    numofp = len(stages)
    for i in range(1, N+1):
        if numofp != 0:
            fail_num = stages.count(i)
            n_stage[i] = fail_num/numofp
            numofp -= fail_num
        else:
            n_stage[i] = 0
    print(n_stage)
    result = sorted(n_stage, key=lambda x:n_stage[x], reverse=True)
    return result