"""
Dictionary

K,V 구조
연관배열 또는 해시
Hash-C, Map-java, Object-javascript, JSON

1. 추가
    딕셔너리이름[키] = 벨류
2. 삭제
    del 딕셔너리이름[키]
"""

dic = {'name':'Eric', 'age':15}
print(dic['name'])

a = {'age' : 18 , 'address' : 'seoul'}

a['name'] = '익명'
del a['name']

print(a.keys())
print(a.values())
for k in a.keys() : print(k)

#인덱스에 바로 접근하는방식 일 시, 키가 없으면 오류남
print(a['age']) 
#.get()함수로 가져오면 None으로 나오며, get(키, '없을때 치환할 값')도 가능
print(a.get('없음', '없음')) 

#in을 사용하여 해당 키 값이 있는지 확인 가능
print(4 in a)


print("================")
"""
Set
집합
"""

l = [1,2,2,3,4,4,5,5]
s1 = set(l)
s2 = set([4,5,6,7,8,4])

#문자열을 set에 넣으면 순서 쪼개지며 중복 제거하고
#한글자씩 집합으로 들어감
s = set("hello")
print(s)

#교집합 구하기: &
print(s1&s2)
print(s1.intersection(s2))

#합집합 구하기: |
print(s1|s2)
print(s1.union(s2))

#차집합 구하기: -
print(s1-s2)
print(s1.difference(s2))

#하나 추가: add
s1.add(6)
print(s1)

#여러개 추가: update
s2.update([1,2,3])
print(s2)

#삭제: remove
s2.remove(2)
print(s2)