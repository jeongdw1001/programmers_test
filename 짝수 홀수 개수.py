# 문제
# 정수가 담긴 리스트 num_list가 주어질 때, 
# num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 
# return 하도록 solution 함수를 완성해보세요.

# 내 풀이
def solution(num_list):
    even = 0
    odd = 0
    for i in num_list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return [int(even), int(odd)]

# 다른 풀이1
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer

# 다른 풀이2
def solution(num_list):
    odd = sum(1 for n in num_list if n % 2)
    return [len(num_list) - odd, odd]

# 다른 풀이3
def solution(num_list):
    answer = [0,0]

    for num in num_list:
        if num % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1

    return answer