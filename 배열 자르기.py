# 내 풀이
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

# 다른 풀이
def solution(numbers, num1, num2):
    answer = []
    for i in range(num1, num2+1):
        answer.append(numbers[i])
    return answer