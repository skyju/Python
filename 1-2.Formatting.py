"""
- formatting
    : %d, %s 로 지정, 변수 이름 지어주고 넣거나, 바로 넣거나 가능
    : {}로 .format사용, 마찬가지로 변수이름 지어주거나 바로 지정 가능
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
: 다른 언어와 마찬가지로 절사 표현은 똑같음
"""

f = "%0.4f" % 3.1415926
print(f)

"""
@중요@: regexp관련 기능을 간단하게 구현가능

"문자열".count(a) : 해당 문자열에 a가 몇개인지 셈
"문자열".find(a) : 해당 문자열에 a의 위치(인덱싱)찾음 없으면 -1
"-".join("abc") : -기준으로 괄호를 결합 // a-b-c

java의 upperCase()가 upper()
java의 trim()이 strip()

replace, split은 같음
"""

g = "-".join("abc")
print(g)