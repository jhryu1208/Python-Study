# Chapter 04_1
# 파이썬 제어문
# IF 실습

## Atom에서 한글이 깨질 때 넣는 코드
import sys
import io

sys. stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys. stdout = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


# [기본 형식]
print(type(True))   ## 0이 아닌수, "abc", [1, 2, 3], (1, 2, 3), ...
print(type(False))  ## 0, " ", [], (), {}, ... (비어있다)

# [ex1]
if True:            ## True일 경우 하단 라인이 시행된다.
    print('Good')

if 'a':             ## 'a'는 True로 인정하여 하단 라인이 실행된다.
    print('Good')

if False:           ## False일 경우 시행되지 않는다.
    print('Bad')

print()


# [ex2]
if False:
    print('Bad!')
else:
    print('Good!')

if True:
    print('Good!')
else:
    print('Bad!')

print()


# [관계 연산자]
# >, >=, <, <=, ==, !=

x = 15
y = 10
print(x == y)   # 양 변이 같은 경우 참          # False
print(x != y)   # 양 변이 다를 때 참            # True
print(x > y)    # 왼쪽이 클때 참                # True
print(x >= y)   # 왼쪽이 크거나 같을 떄 참      # True
print(x < y)    # 오른쪽이 클때 참              # False
print(x <= y)   # 오른쪽이 크거나 같을 때 참    # False

# [ex3]
city = ""
if city:
    print("You are in :", city)
else:
    print("Please enter your city")

print()


# [ex4]
city2 = "Seoul"
if city2:
    print("You are in :", city2)
else:
    print("Please enter your city")

print()


# [논리연산자(중요)]
# and, or, not

a = 75
b = 40
c = 10

print('and : ', a > b and b > c)    ## a > b > c
print('or : ', a > b or b > c)      ## 앞에서 True이면 뒤에껀 판별 x, 앞에서 False이면 뒤에가 True, False인지 판별
print('not : ', not a > b)          ## 반대로 출력, False
print('not : ', not b > c)          ## False
print('not : ', not True)
print('not : ', not False)

print()


# [산술, 관계, 논리 우선순위]
# 산술 > 관계 > 논리
print('e1 : ', 3 + 12 > 7 + 3)                  ## '+' (산술 연산자) > '>' (관계 연산자)
print('e2 : ', 5 + 10 * 3 > 7 + 3 * 20)         ## '*,+' (산술 연산자) > '>' (관계 연산자)
print('e3 : ', 5 + 10 > 3 and 7 + 3 == 10)      ## '+' (산술 연산자) > '>, ==' (관계 연산자) > 'and'(논리 연산자)
print('e4 : ', 5 + 10 > 0 and not 7 + 3 == 10)  ## '+' (산술 연산자) > '>, ==' (관계 연산자) > 'and, not'(논리 연산자)

print()

# [ex5]
score1 = 90
score2 = 'A'
## 복수의 조건이 모두 참일 경우에 실행
if score1 >= 90 and score2 == 'A':
    print('Pass')
else :
    print('Fail')

# [ex6]
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin':
    print('관리자 입장')

if id2 == 'admin' and grade == 'platinum':
    print('최상위 관리자')

# [다중 조건문]

num = 90

if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('과락')

print()


# [중첩 조건문]
grade = 'A'
total = 95
if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    else:
        print('장학금 50%')
else:
    print('장학금 없음')

print()


# [in, not in]
q = [10, 20, 30]                                    ## 리스트
w = {70, 80, 90, 100}                               ## 집합
e = {"name": "Lee", "city": "Seoul", "grade" : "A"} ## 딕셔너리
r = (10, 12, 14)                                    ## 튜플

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)          ## 딕셔너리에서 in은 키값을 식별함
print("Seoul" in e)         ## 따라서, value값을 식별하고 싶을때 in을쓰면 있어도 false가 나오므로
print("Seoul" in e.values())   ## in을 이용해 특정 value값을 식별하고 싶을떄는 .values() method를 이용한다.
