# 내 풀이
str = input()
print(str.swapcase())


# 다른 풀이
str = input()
answer   = ''
for a in str:
    if a.isupper():
        answer = a + s.lower()
    else:
        answer = a + s.upper()
print(answer)


# 다른 풀이