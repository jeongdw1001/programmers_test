# 내 풀이 1
def solution(n):
    answer = []
    for i in range(1,n+1):
        if i % 2 == 1:
            answer.append(i)

# 내 풀이 2
def solution(n):
    return [i for i in range(1, n+1, 2)]