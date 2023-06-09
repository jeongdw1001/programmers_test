# 내 풀이
def solution(num_list, n):
    num_list = num_list[n:] + num_list[:n]
    return num_list