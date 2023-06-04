# 내 풀이

def solution(number):
    a = list(map(int, str(number)))
    return sum(a) % 9

# 다른 풀이 1
def solution(number):
    return int(number) % 9

# 다른 풀이 2
def solution(number):
    return sum([int(i) for i in number]) % 9