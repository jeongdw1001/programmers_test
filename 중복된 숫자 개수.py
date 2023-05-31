# 내 풀이
def solution(array, n):
    return array.count(n)

# 다른 풀이 1
def solution(array, n):
    answer = 0
    for i in range(0,len(array)):
        if n == array[i]:
            answer += 1
    return answer