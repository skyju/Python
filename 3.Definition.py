# 함수 def
def sum(a, b):
    return a+b

print(sum(3, 2))

# 가변 인자 함수 만들기
# *args arguments 약자로 많이 씀
def sum_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum_many(1, 2, 3, 4, 5, 6, 7))

# 키워드 피라미터
# 여러개의 매개변수를 만들어서 딕셔너리를 만들겠다는 의미
# **kwargs :key word arguments , dictionary(k,v)가 들어옴
def print_names(**kwargs):
    for k, v in kwargs.items():
        if(k == "name"):
            print("당신의 이름은 "+v)


a = {"name": "박지성", "age": 11}
print_names(**a)
print_names(name="박지성", age=11)

# 기본값 설정 함수
def say_myself(name, old, sex=True):
    print("나의 이름은 %s 입니다." % name, end=" ")
    print("나이는 %d살 입니다." % old, end=" ")
    if sex:
        print("여자입니다.")
    else:
        print("남자입니다.")

say_myself("이민수", 20)
say_myself("김민식", 33, 0)
say_myself(old=77, sex=False, name="권경춘")

# 전역변수, 지역변수
a = 1

def vartest():
    global a
    a += 1

vartest()
print(a)

# lambda식 표현
# def add(a,b):
#   return a+b
def add(a, b): return a+b
print(add(1, 2))

myList = [lambda a, b: print(a+b), lambda a, b: print(a-b)]
myList[1](7,2)

#입출력 기본 함수 input, print

number = input("숫자를 입력해주세요")
print(number)

#알아서 붙여서 출력해줌 
print("Life " "is " "Cool")