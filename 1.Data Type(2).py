"""
List

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
