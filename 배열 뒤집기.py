# 내 풀이
def solution(num_list):
    num_list.reverse()
    return num_list

# 다른 풀이1
def solution(num_list):
    return num_list[::-1]

# 다른 풀이2
def solution(num_list):
    result = []
    while(num_list):
        result.append(num_list.pop())
    return result