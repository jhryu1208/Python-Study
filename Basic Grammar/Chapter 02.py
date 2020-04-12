# Chpater 02
# 파이썬 기초
# 파이썬 변수

# [기본 선언]
## n이 있는 주소로 찾아가서 n에 할당되어 있는 값을 출력
n = 700
print (n)
print (n*700)

## type()예약어를 이용해서 n이라는 변수에 할당된 값의 자료형을 알아낼 수 있다.
print (type(n))

print()

# [동시 선언]
x=y=z=700
print(x,y,z)

print()

# [재선언]
## 마지막에 선언된 값이 기존에 선언된 값을 덮어쓴다 (재할당한다.).
var = 75
var = "Change Value"

print (var)
print (type(var))

print()

# [Object References]
## 변수 값 할당 상태
## 1. 타입에 맞는 오브젝트를 생성
## 2. 값 생성
## 3. 콘솔 출력

## 예1)
print(300)
print(int(300))

## 예2)
## n->700
print(n,type(n))
print()

## m->700<-n
m=n
print(m, n)
print(type(m), type(n))
print()

## 재할당
m = 400
print(m, n)
print(type(m), type(n))
print()

# [id(identity)확인] : 객체의 고유값 확인

m=800
n=655

## 다른 오브젝트를 참조
## 다른 값을 할당했을 때는 서로 다른 고유값을 가진다.
print(id(m))
print(id(n))
print(id(m)==id(n))
print()

m=800
n=800

## 같은 오브젝트를 참조
## 같은 값을 할당했을 때는 서로 같은 고유값을 가진다.
print(id(m))
print(id(n))
print(id(m)==id(n))
print()

# [다양한 변수 선언]

## Camel Case : 처음에는 소문자, 이어지는 글자의 첫글자는 대문자로 시작 -> Method
## ex) numberOfCollegeGraduates

## Pascal Case : 첫글자 대문자, 이어지는 글자의 첫글자 또한 대문자로 시작 -> Class
## ex) NumberOfCollegeGraduates

## Snake Case : 뱀처럼 이어지는 영어단어를 _(밑줄)로 연결해준다, 모든 글자는 소문자 -> 변수
## ex) student_grade

## 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

## 예약어는 변수명으로 불가능
## ex) for, as, class
## ===================================
## False	def	if	raise
## None	del	import	return
## True	elif	in	try
## and	else	is	while
## as	except	lambda	with
## assert	finally	nonlocal	yield
## break	for	not
## class	from	or
## continue	global	pass
## ===================================
