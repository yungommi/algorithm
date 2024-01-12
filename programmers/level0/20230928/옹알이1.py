# 예상 시간복잡도: O(ABC^2)

def solution(babbling):
    says = ["aya", "ye", "woo", "ma"]
    result = 0
    for i in range(len(babbling)):
        for say in says:
            if (say in babbling[i]) and (say*2 not in babbling[i]):
                babbling[i] = babbling[i].replace(say, "*")
        if all(char == "*" for char in babbling[i]):
            result += 1
    return result
