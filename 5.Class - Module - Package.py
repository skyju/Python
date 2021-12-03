# Class?
# 반복되는 변수& 메서드(함수)를 미리 정해놓은 틀(설계도)

class Calculator:
    def __init__(self):
        self.result = 0
    def sum(self,num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

cal1.sum(3)
cal2.sum(4)
print(cal2.sum(3))
print(cal1.sum(3))