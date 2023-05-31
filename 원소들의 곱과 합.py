# 문제
# 정수가 담긴 리스트 num_list가 주어질 때,
# 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을
# 크면 0을 return하도록 solution 함수를 완성해주세요.


# 내 풀이
from functools import reduce

def solution(num_list):
    mul = reduce(lambda x, y : x * y, num_list)
    hap = sum([i for i in num_list])
    if mul < hap*hap:
        return 1
    elif mul > hap*hap:
        return 0

# 다른 풀이1
def solution(num_list):
    mul = 1
    for i in num_list:
        mul *= i

    if mul < sum(num_list)**2:
        return 1
    else:
        return 0

# 다른 풀이2
#from functools import reduce

def solution(num_list):
    return 1 if reduce(lambda x,y : x*y, num_list) < sum(num_list)**2 else 0

