# 문제
# 함수 solution은 정수 n을 매개변수로 입력받습니다.
# n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
# 예를들어 n이 118372면 873211을 리턴하면 됩니다.

# 내 풀이
def solution(n):
    answer = [i for i in str(n)]
    answer.sort(reverse = True)
    return int(''.join(answer))

# 다른 풀이 1
def solution(n):
    return int(''.join(sorted(list(strn(n)),reverse = True)))

# 다른 풀이 2
def solution(n):
