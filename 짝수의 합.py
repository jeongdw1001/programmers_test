# 내 풀이
def solution(n):
    answer = 0
    for i in range(2,n+1,2):
        answer += i
    return answer

# 다른 풀이1
def solution(n):
    return sum([i for i in range(2, n+1, 2)])

# 다른 풀이2
def solution(n):
    return 2*(n//2)*((n//2)+1)/2

# 다른 풀이3
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            answer += 1
    return answer