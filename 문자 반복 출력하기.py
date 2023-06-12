# 내 풀이
def solution(my_string, n):
    answer = ''
    for i in range(0,len(my_string)):
        answer += my_string[i]*n
    return answer

# 다른 풀이
def solution(my_string, n):
    return ''.join(i*n for i in my_string)

# 다른 풀이2
def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += (i*n)
    return answer