# 내 풀이
def solution(start, end):
    list = []
    for i in range(start, end+1):
        list.append(i)
    return list

# 다른 풀이1
def solution(start, end):
    return list[range(start, end+1)]

# 다른 풀이2
def solution(start, end):
    return [i for i in range(start, end+1)]