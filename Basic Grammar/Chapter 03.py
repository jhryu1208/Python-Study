# Chpater 02
# 파이썬 기초
# 숫자형

# [파이썬 지원 자료형]
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린 (True/False)
str : 문자열 (시퀀스)
list : 리스트 (시퀀스)
tuple : 튜플 (시퀀스)
set : 집합
dict : 사전
"""

# [데이터 타입]
str1 = "Python"
bool = True
str2 = 'Anaconda'

## 10 == 10.0? 사람입장에서는 같지만 둘은 다르다.
float_v = 10.0
int_v = 7

## list는 대괄흐를 사용
list = [str1, str2]
print(list)

## dict(사전타입)는 중괄호를 이용
## Machine Learning을 꺼내기위해서는 name이라는 키가 필요
## 2.0을 꺼내기위해서는 version이라는 키가 필요
dict ={
"name": "Machine Learning",
"version": 2.0
}

## tuple은 소괄호를 사용
## 또는 소괄호 없이 ,(콤마)로만 이어 갈 수 있다.
## ex) tuple = 7, 8, 9
tuple =(7,8,9)

## set은 중괄호를 사용
set ={3,5,7}

print()


# [데이터 타입 출력]
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))


# [숫자형 연산자]
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) 절대값
pow(x,y) or x ** y -> pow(2,3)=2**3
"""

# [정수선언]
i = 77
i2 = -14
## 다른 객체지향 언어에 비해 큰수 넣기 편함... 엄청편한부분...
big_int=7777777777777777777777777777799999999999999999999999


# [정수출력]
print(i)
print(i2)
print(big_int)
print()

# [실수선언]
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

# [실수출력]
print(f)
print(f2)
print(f3)
print(f4)

print()

# [연산실습]
i1 = 39
i2 = 939
big_int1 = 153341287461829374618923746198273
big_int2 = 31248973264871263489123764189723468712
f1 = 1.234
f2 = 3.9412

# [+]
print(">>>>> +")
print("i1 + i2 : ", i1 + i2)
print("f1 + f2 : ", f1 + f2)
print("big_int1+big_int2 : ", big_int1 + big_int2)

print()


# [*]
print(">>>>> *")
print("i1 + i2 : ", i1 * i2)
print("f1 + f2 : ", f1 * f2)
print("big_int1+big_int2 : ", big_int1 * big_int2)

# [형 변환 실습]
## b를 제외한 나머지는 실수
a = 3.
b = 6
c = .7
d = 12.7
## 타입출력
print(type(a))
print(type(b))
print(type(c))
print(type(d))
## 형변환
## 6에서 6.0으로 실수 형변환됨
print(float(b))
## 0.7에서 0으로 정수 형변환됨
print(int(c))
## 12.7에서 12로 정수 형변환됨
print(int(d))
## True : 1, False : 0
print(int(True))
## 0에서 0.0으로 실수 형변환됨
print(float(False))
## 3에서 3+0j로 복소수 형변환됨
print(complex(3))
## 복소수함수는 숫자를 받아야하는데 문자(문자형)을 받아도
## 내부적으로 문자형을 숫자형으로 바꿔서 실행한다.
## 문자형 3에서 복소수형 3+0j 로 형변환되었다.
print(complex('3'))
print(complex(False))

print()


# [수치 연산 함수]
## 절대값
print(abs(-7))
## (중요) divmode(x,y)
## 100을 8로 나누면 x와 y에 각각 몫과 나머지를 입력한다.
x,y=divmod(100,8)
print(x,y)
## 승수
print(pow(5,3),5**3)

print()


# [외부 모듈]
## import를 이용해 math라는 패키지를 가져옴
import math
## math 패키지안에있는 pi를 호출
## 원주율이 출력
print(math.pi)
## x이상의 수 중에서 가장 작은 정수를 찾아줌
## 5.1 보다 큰 정수 중에서 가장 작은 정수 = 6
print(math.ceil(5.1))
