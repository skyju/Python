"""
<자료형>
1. 숫자
2. 문자열
3. bool
4. variable
5. List
6. Tuple
7. Dictionary
8. Set

type()을 통해 자료형을 확인


1. 숫자

key!: 
    - /
    :자바에서는 /가 몫계산이지만 파이썬에서는 //가 몫계산
    파이썬에서는 몫+나머지 다나옴
    - **
    : ^* 승계산 의미

2. 문자

key!:
    - 문자*수
    : 해당 문자를 수만큼 출력하라
    : javasciprt에서는 NaN, java에서는 문자열*수 오류, char*수 아스키코드 반환

    - Indexing
    : java에서 하는 String에 대한 char[] 접근을 빠르게 할 수있음
    : 음수로 하면 역방향으로 지정된다.

    - Slicing
    : a[이상:미만:간격]
    : a[::-1] 뒤로 읽으라는 뜻
    
"""
a = "Life is cool"
print(a[-1])
print(a[:8])
print(a[::-1])

"""
3. bool

"문자열" 참
"" 거짓
[1,2,3] 참
[] 거짓
() 거짓
{} 거짓
1 참
0 참
None 거짓

"""

a = [1, 2, 3, 4]
while a:
    print(a)
    a.pop()


# 파이썬의 특징적 변수 할당
a, b = 1, 2
print(a)
print(b)

(a, b) = 1, 2
print(a)
print(b)

a = b = 'hello'
print(a)
print(b)

#변수값 서로 바꾸기(Tuple활용)
a = 'a'
b = 'b'
a,b = b,a
print(a)
print(b)
