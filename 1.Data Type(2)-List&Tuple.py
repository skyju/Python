"""
List

0. list에는 c 포인터 개념이 있어서 주의해야함
    - 원천값을 바꾸고 싶지않다면 슬라이싱해서 갖고오거나
    - copy모듈 사용하여 copy()함

1. +: 연결되어서 나옴
2. *: 하기 하면 같은 리스트가 여러번 나옴

3. slicing: list에 indexing이 있기 때문에 slicing도 당연히 됨

4. 삭제: a[0:1] = [] 빈 리스트로 교체 또는 del a[0]
    - .remove(삭제할값) : 여러개면 가장 앞에있는거만 사라짐
5. 추가: 
    - .append(추가할내용) : 맨 뒤에 추가됨
    - .insert(추가할 인덱스 위치, 추가할내용)

6. 정렬: .sort()
7. 뒤집기: .reverse()
8. 빼내기: .pop() 마지막꺼를 빼냄
9. 개수 세기: .count(셀 대상)

10. 리스트 확장: .extend([추가할 배열])

"""
#포인터개념
x = [1,2,3]
y = x #b에 x리스트 주소가 들어감
x[0] = 2
print(y)

#원천값을 건드리고 싶지 않다면, 슬라이싱하면됨
x = [1,2,3]
y = x[:]
x[0] = 2
print(y)

#copy모듈 사용하기
x = [1,2,3]
from copy import copy
y = copy(x)
x[0] = 4
print(y)

print("===========")

#슬라이싱 실습
a = [1,2,3]
b = [4,5,6]
del b[0]
a[0:1] = []

print(a[0])

a.insert(0,1)

c = a+b
d = c[0:4]*2
d.sort()
d.reverse()
print(d)

"""
Tuple
: 자물쇠가 잠긴 List, 변경 추가 삭제 불가능

: 더하기 곱하기는 가능하지만, 튜플이 변화하는게 아니고
결과로 새로운 튜플이 나오는 것..
"""

t1 = (1,2,'a','b')
print(t1[0]+1)
a = (1,2)
a = a*3
print(a)