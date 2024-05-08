tmp = '0123456789abcdefghijklmnopqrstuvwxyz'
def convert(num, base):
    q_, r_ = divmod(num,base)
    if q_ == 0: 
        return tmp[r_]
    else: 
        return convert(q_,base) + tmp[r_]
    
def prime_num(n):
    for i in range(2,n):
        if n % i == 0:
            return 0
        return 1
    
def solution(n, k):
    converted = str(convert(n,k))
    print(converted)
    temp = converted.split('0')
    print(temp)
    answer = 0 
    for x in temp:
        if len(x)>0:
            if int(x)>1:
                print(x)
                answer += int(prime_num(int(x)))
    print(answer)
    return answer
