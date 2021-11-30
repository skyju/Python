"""
<자료형>
1. 숫자
2. 문자열
3. boolean
4. variable
5. List
6. 튜플
7. 딕셔너리
8. 집합

type()을 통해 확인
"""

"""
1. 숫자

key!: 
자바에서는 /가 몫계산이지만 파이썬에서는 //
파이썬에서는 몫+나머지 다나옴

** 는 ^*
"""

"""
2. 문자

key!: 
- 문자*수
javascript에서는 NaN
java에서는 String*수는 안되고, char*수 일 시 아스키 코드로 나오지만
파이썬에서는 해당 문자를 수만큼 출력하라 이다.

인덱싱:
java에서 하는 String에 대한 char[] 접근을 빠르게 할 수있음
음수로 하면 역방향으로 지정된다.

슬라이싱
a[이상:미만:간격]
a[::-1] 뒤로 읽으라는 뜻
"""
a = "Life is cool"
print(a[-1])
print(a[:8])
print(a[::-1])

"""
- formatting
"""
number = 10
day = 3
b = "I ate %d apples. so I was sick for %s days" % (number, day)
print(b)

c = "hello everyone my name is %s and {hello}".format(
    hello="nice too meet you.") % "kate"
print(c)

name = "katy"
d = f"My name is {name}"
print(d)

"""
소수점 표현
"""

f = "%0.4f" % 3.1415926
print(f)

"""
"문자열".count(a) : 해당 문자열에 a가 몇개인지 셈
"문자열".find(a) : 해당 문자열에 a의 위치(인덱싱)찾음 없으면 -1
"-".join("abc") : -기준으로 괄호를 결합 // a-b-c

java의 upperCase()가 upper()
java의 trim()이 strip()

replace, split은 같음
"""

g = "-".join("abc")
print(g)