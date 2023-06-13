# 다른 풀이 1
def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())


# 다른 풀이 2
def solution(my_string, alp):
    return ''.join([i.upper() if i==alp else i for i in my_string])

# 다른 풀이 3
def solution(my_string, alp):
    result = ''
    for i in my_string:
        if i == alp:
            result += i.upper()
        else:
            result += i
    return result