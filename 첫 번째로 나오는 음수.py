# 내 풀이
def solution(num_list):
    for i, num in enumerate(num_list):
        if num < 0:
            return i
    return -1

# 다른 풀이 1
def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1