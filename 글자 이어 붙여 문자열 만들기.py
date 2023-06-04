# 내 풀이
def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer += my_string[i]
    return answer

# 다른 풀이1
def solution(my_string, index_list):
    return ''.join([my_string[i] for i in index_list])

# 다른 풀이2
def solution(my_string, index_list):
    list = []
    for i in index_list:
        list.append(my_string[i])
    
    return ''.join(list)