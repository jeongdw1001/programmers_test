# 내 풀이
def solution(numbers):
    return sum(numbers) / len(numbers)

# 다른 풀이1
def solution(numbers):
    sum = ''
    for i in numbers:
        sum += i
    ans = sum / len(numbers)
    return ans