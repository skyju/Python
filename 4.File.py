# 파일 생성하기
#f = open("새파일.txt", 'w')
#f.close()

# 파일 읽고 쓰기
# r:읽기 모드: 파일을 읽기만 할 때 사용
# w:쓰기 모드: 파일에 내용을 쓸 때 사용
# a:추가 모드: 파일의 마지막에 새로운 내용을 추가 시킬 때 사용

# 쓰기모드
# 파일을 쓰기 모드로 열어서 출력값 적기
f = open("새파일.txt", 'w', encoding="UTF-8")
for i in range(1,11):
    data = "%d번째 줄입니다\n" %i
    f.write(data)
f.close()

# 읽기모드
# readline()
f = open("새파일.txt", 'r', encoding="UTF-8")
while True:
    line = f.readline()
    if not line: break
    print(line, end="")
f.close()

# readlines() 활용
f = open("새파일.txt", 'r', encoding="UTF-8")
lines = f.readlines()
for line in lines: 
    print(line.strip("\n"))
f.close()

# read() 활용
f = open("새파일.txt", 'r', encoding="UTF-8")
data = f.read()
print(data)
f.close()

# 추가 모드
f = open("새파일.txt", 'a', encoding="UTF-8")
for i in range(11,20):
    data = "%d번째 줄이 추가됩니다\n" %i
    f.write(data)
f.close()

# with문과 함께 close하기 with as
with open("새파일.txt", 'w', encoding="UTF-8") as f:
    f.write("Life is Cool, Isn't it?")
# 새 파일을 열어서 지역변수 f에 저장하여 사용