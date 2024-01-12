# 예상 시간복잡도: O(n)

def solution(numbers):
    nums = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    ]
    for i, num in enumerate(nums):
        numbers = numbers.replace(num,str(i))
    return int(numbers)