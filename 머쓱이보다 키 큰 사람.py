# 내 풀이
def solution(array, height):
    answer = 0
    array.sort(reverse=True)
    for i in array:
        if height < i:
            answer += 1
    return answer

# 다른 풀이
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)