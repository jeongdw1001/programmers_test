# 내 풀이
def solution(n):
    answer = 0
    for i in range(1,n+1,7):
        answer += 1
    return answer

# 다른 풀이1
def solution(n):
    return (n - 1) // 7 + 1