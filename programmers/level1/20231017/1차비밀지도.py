# 예상 시간복잡도: O(N^2)

def solution(n, arr1, arr2):
    ans = []
    for i in range(n):
        tmp1 = str(bin(arr1[i])[2:])
        tmp2 = str(bin(arr2[i])[2:])
        tmp1 = '0'*(n-len(tmp1)) + tmp1
        tmp2 = '0'*(n-len(tmp2)) + tmp2
        tmp = ''
        for k in range(n):
            if tmp1[k]=='1' or tmp2[k]=='1':
                tmp +='#'
            else:
                tmp += ' '
        ans.append(tmp)
    return ans

