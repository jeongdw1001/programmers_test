# 내 풀이
def solution(my_string):
    for i in ('a','e','i','o','u'):
        my_string = my_string.replace(i,'')
    return my_string

# 다른 풀이 1
def solution(my_string):
    return ''.join([i for i in my_string if not(i in "aeiou")])

# 다른 풀이 2
def solution(my_string):
    collections = ['a','e','i','o','u']
    for i in collections:
        my_string = my_string.replace(i,'')
    return my_string