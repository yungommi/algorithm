# 예상 시간복잡도: O(N)

def solution(id_list, report, k):
    dict_ = {}
    num_of_report = {}
    mail_receive = {}
    for id in id_list:
        dict_[id] = []
        num_of_report[id] = 0
        mail_receive[id] = 0
    for i in report:
        temp = i.split()
        if temp[1] not in dict_[temp[0]]:
            dict_[temp[0]].append(temp[1])
            num_of_report[temp[1]] +=1 
    out = []
    for id in id_list:
        if num_of_report[id] >= k:
            out.append(id)
    answer = [0]*len(id_list)
    for i in range(len(id_list)):
        id_ = id_list[i]
        for x in dict_[id_]:
            if x in out:
                answer[i]+=1
    return answer

    