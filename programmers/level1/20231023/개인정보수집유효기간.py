# 예상 시간복잡도: O(N)

def date_comparison(expiration_date, today):
    if expiration_date[0] > today[0]:
        return True
    if expiration_date[0] == today[0] and expiration_date[1] > today[1]: 
        return True
    if expiration_date[0] == today[0] and expiration_date[1] == today[1] and expiration_date[2] > today[2]:
        return True
    return False
   
def solution(today, terms, privacies):
    result = []
    i = 1
    today = list(map(int,today.split(".")))
    expiration = {term[0]:int(term[2:]) for term in terms}
    for pri in privacies:
        pri = pri.split()
        pri_date = list(map(int,pri[0].split(".")))
        pri_date[1] += expiration[pri[1]]
        if (pri_date[1] > 12):   
            if (pri_date[1] % 12 == 0):
                pri_date[0] += (pri_date[1] // 12) - 1 
                pri_date[1] = 12 
            else:    
                pri_date[0] += pri_date[1] // 12 
                pri_date[1] %= 12 
        if date_comparison(pri_date, today) == False : 
            result.append(i) 
        i += 1
    return result
