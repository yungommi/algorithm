# 예상 시간 복잡도 O(NlogN)
import math 
def solution(fees, records):
    stay = {}
    for x in records:
        tmp = x.split()
        time = tmp[0].split(":")
        minute = int(time[0])*60 + int(time[1])   
        if tmp[2]=='IN':
            minute *= -1 
        if tmp[1] in stay:
             stay[tmp[1]] += minute 
        else: 
            stay[tmp[1]] = minute
    for x in stay:
        if stay[x] <=0 :
            stay[x] += (23*60+59)
    new = sorted(stay.items())
    ans = []
    for car,time in new:
        if time <= fees[0]:
            ans.append (fees[1])
        else:
            time -= fees[0]
            time_ = math.ceil(time/fees[2])
            ans.append(fees[1]+fees[3]*time_)
    return ans

