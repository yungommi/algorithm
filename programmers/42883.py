def solution(number, k):
    l = ['9']
    i = 0 
    while k>0:
        if number[i] <= l[-1]:
            l.append(number[i])
            i += 1
        else:
            l.pop()
            k -= 1 
        if i == len(number):
            return number[:len(number)-k]
            
    answer = "".join(l[1:]) + number[i:]
    
    return answer