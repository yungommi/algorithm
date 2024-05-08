# 2839 
# greedy 

n = int(input())
def function(n:int):
    rem = n % 5
    val = n // 5
    if rem == 0 :
        return val
    elif rem == 1:
        if val < 1:
            return -1
        else:
            return(val-1+2)
    elif rem == 2:
        if val < 2:
            return -1
        else:
            return(val-2+4)
    elif rem == 3:
        return(val+1)
    else:
        if val<1:
            return -1
        else:
            return(val-1+3)
        
print(function(n))