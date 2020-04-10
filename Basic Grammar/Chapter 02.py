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

# 예1)
print(300)
print(int(300))

# 예2)
## n->700
print(n,type(n))
print()

## m->700<-n
m=n
print(m, n)
print(type(m), type(n))
print()

m = 400
print(m, n)
print(type(m), type(n))
print()
