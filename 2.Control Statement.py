"""
<조건문>

python에서는 tab 정렬하는 게 중요하다.
들여쓰기 유의


python에서는 ||, &&를
or, |
and, &
로씀


좌항에 찾을 값, 우항에 찾을 배열, (튜플이나 리스트)
int
not in


elif: 다른 언어의 else if

"""

money = 2000
card = 1
if (money >= 3000):
    print('택시 타고 가라')
elif card:
    print('카드로 택시타고 가라')
else:
    print('걸어가라')

if 1 in [1, 2, 3]:
    print('1이 있습니다.')


# 조건식 표현식 : 다른 언어의 삼항연산자 표현방법
# true일때 실행할 문장 if문 else false일때 실행할 문장
# 조건문? 참:거짓 > java의 삼항연산자

score = 70
message = "success" if score >= 60 else "faliure"
print(message)


"""
<반복문>

- 증감연산자 python에서 안씀
- Debugging이랑 breakpoint사용해서 확인 가능(run쪽에)

"""
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")

# break 실습
coffee = 10
money = 300
while money:
    print("돈을 받았으니까 커피를 드립니다.")
    coffee -= 1
    print("남은 커피의 양은 %d개입니다" % coffee)
    if not coffee:
        print("커피 sold Out~")
        break

# continue 실습 : 홀수만 찍기
a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)

# for 변수 in 리스트(또는 튜플, 문자열)
#   수행할 문장
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1, 2), (3, 4), (5, 6)]
for(first, last) in a:
    print(first)
    print(last)

# java에서의 향상된 for문 (for each문)과 유사하다.
marks = [90, 25, 67, 45, 80, 99]
number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue
    else:
        print("%d번 학생은 합격입니다" % number)

# 다른 언어에서의 횟수 반복 for문 하는 법: range()함수
sum = 0
for i in range(1, 11):
    sum += i
print(sum)

# 2중 for문 작성
# print함수의 end옵션,, end기준으로 나뉘어 나옴 기본은 \n
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')

# 유의깊게 볼 것
# 리스트 내포 방식
a = [1,2,3]
result1 = [num*3 for num in a if num % 2 == 0]
print(result1)

""" 풀어쓰자면
result = []
for num in a:
    if num % 2 == 0:
        result.append(num*3)
"""

# 2중 for문 한줄로
result2 = [x*y for x in range(2, 10) for y in range(1, 10)]
for i in result2: print(i, end=" ")