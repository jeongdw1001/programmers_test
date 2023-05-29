# 내 풀이
def solution(my_string):
    return ''.join(reversed(my_string))

# 다른 풀이1
def solution(my_string):
    return my_string[::-1]

# 다른 풀이2
def solution(my_string):
    answer = ''

    for i in range(len(my_string)-1,-1,-1):
        answer += my_string[i]
    
    return answer
