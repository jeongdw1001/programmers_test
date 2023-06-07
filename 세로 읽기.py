# 내 풀이
def solution(my_string, m, c):
    answer = [my_string[i] for i in range(c-1, len(my_string), m)]
    return ''.join(answer)

# 다른 풀이
def solution(my_string, m, c):
    return my_string[c-1::m]

