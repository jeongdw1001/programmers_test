# 내 풀이
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i] == True:
            answer += (a + i * d)
    return answer

# 다른 풀이 1
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
            answer += (a + i * d) * int(included[i] )  # 0, 1로 변환
    return answer


# 다른 풀이 2
# 리턴값에 조건문 함축시켜서 풀이
def solution(a, d, included):
    return sum([(a + i *d) for i in range(len(included) if included[i]])


# 다른 풀이 3
def solution(a, d, included):
    list = []
    for i in range(len(included)):
        if included[i] == True:
            list.append(a + i * d)
    return sum(list)