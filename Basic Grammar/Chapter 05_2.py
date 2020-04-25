# Chapter05_2
# 파이썬 사용자 입력
# Input 사용법
# 기본 타입(str)

# [예제1]
name = input("Enter Your Name : ")
grade = input("Enter Your Grade : ")
company = input("Enter Your Company Name : ")

print(name, grade, company)

# [예제2]
number = input("Enter Number : ")
name = input("Enter Name : ")

## 숫자를 넣든 문자를 넣든 str타입으로 출력된다.
## 따라서, number * 3에서 number는 아무리 숫자라도 정수형 타입이 아니기에
## 계산되는 것이 아니라, 문자형의 특징으로, 해당 숫자가 세번 출력된다.
print("Type of Number", type(number), number * 3)
print("Type of Name", type(name))

# [예제3]
first_number = int(input("Enter number1 : "))
second_number = int(input("Enter number2 : "))
## 하지만, 숫자형 형변환 과정을 지나치면, 계산을 시행할 수 있다.
total = first_number + second_number
print("first_number+second_number : ", total)

# [예제4]
float_number = float(input("Enter a float number : "))
## 마찬가지로, 실수형 변환 가능
## 따라서, input함수는 형변환을 사용해서 이용하는 것이 핵심이다.
print("input float : ", float_number)
print("input type : ", type(float_number))

# [예제5]
print("FisrtName - {0}, LastName - {1}".format
(input("Enter First Name : "),input("Enter Second Name : ") ))
## input먼저 출력 -> print 출력
