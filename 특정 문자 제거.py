# 내 풀이
def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if i != letter:
            answer += i
    return answer

# 다른 풀이1
def solution(my_string, letter):
    return my_string.replace(letter, '')


# 다른 풀이2
def solution(my_string, letter):
    answer = ''
    for i in range(0, len(my_string)):
        if my_string[i] != letter:
            answer += my_string[i]
    return answer