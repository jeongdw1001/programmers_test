# 내 풀이
def solution(num_list, n):
    if n in num_list:
        return 1
    else:
        return 0


# 다른 풀이 1
def solution(num_list, n):
    return int(n in num_list)


# 다른 풀이 2
def solution(num_list, n):
    return 1 if n in num_list else 0