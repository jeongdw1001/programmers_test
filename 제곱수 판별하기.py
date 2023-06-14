# 내 풀이
import math
def solution(n):
    sqrt_num = math.sqrt(n)
    if float(int(sqrt_num)) == sqrt_num:
        return 1
    return 2

# 다른 풀이 1
def solution(n):
    return 1 if (n ** 0.5) % 1 == 0 else 2

# 다른 풀이 2
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2

# 다른 풀이 3
def solution(n):
    if n**(1/2) == int(n**(1/2)) :
        return 1
    else :
        return 2