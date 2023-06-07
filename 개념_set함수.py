# set 선언하기
s = set()
s = set([1,2,3,4])
s = {1,2,3,4}
print(type(s))  # set

s = {}
print(type(s))  # dict

# 중복 삭제 가능
s = set([1,1,1,1,1,1,2,2,2,2,2,5,5,5,5,3,3,3,4,4,4])
print(s)

# 원소 추가 add
a = {100}
a.add(50)
print(a)
a.add(12)
print(a)

# 여러 데이터 한번에 추가 update - 중복은 자동으로 제거
k = {1,2,3}
k.update([3,4,5])
print(k)

# 원소 제거 remove, 없으면 keyerror 발생
k = {1,2,3}
k.remove(3)
print(k)

# discard(item) - item에 해당하는 원소 제거, 없어도 에러 발생 x
k = {1,2,3}
k.discard(3)
k.discard(5)
print(k)