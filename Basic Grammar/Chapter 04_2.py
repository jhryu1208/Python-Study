# Chapter 04_2
# 파이썬 반복문
# FOR 실습

import sys
import io

sys. stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys. stdout = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 코딩의 핵심
# for in <collection>
#    <loop body>

for v1 in range(10):        ## 0 ~ 9
    print('v1 is : ', v1)

print()

for v2 in range(1,11):      ## 1 ~ 10
    print('v2 is : ', v2)

print()

for v3 in range(1,11,2):    ## 1, 3, 5, 7, 9
    print('v3 is : ', v3)

print()


# [1 ~ 1000합]
sum1 = 0
for v in range(1,1001):
    sum1 += v
print('1 ~ 1000 sum : ', sum1)

print('1 ~ 1000 sum : ', sum(range(1,1001)))
print('1 ~ 1000 4의 배수의 합 : ', sum(range(4,1001,4)))

# [Iterables 자료형]
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range, reverse,enumerate, filter, map, zip

# [예제 1 (리스트)]
names = ['kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']
for name in names:
    print('You are : ', name)

print()

# [예제 2 (리스트)]
lotto_numbers  = [11, 19, 21, 28, 36, 37]
for n in lotto_numbers:
    print("Current number : ", n)

print()

# [예제 3 (문자열)]
word = "Beautiful"
for s in word:
    print('word : ',s)

print()

# [예제 4 (딕셔너리)]
my_info = {
    "name": "Lee",
    "Age" : 33,
    "City": "Seoul"
}

for key in my_info:
    print('key : ', key)

for v in my_info.values():
    print('value : ', v)

print()


# [예제 5]
name = 'FineAppLE'

for n in name:
    if n.isupper():             ## isupper() 대문자인지 검사
        print(n)
    else:
        print(n.upper())        ## upper() 소문자를 대문자로 변환

# [break]
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15 , 34, 36, 38]
for num in numbers:
    if num == 34:
        print('Check : 34!')
        break
    else:
        print('Pass', num)

print()


# [continue]
lt = ["1", 2, 5, True, 4.3, complex(4)]
for v in lt:
    if type(v) is bool:                      ## 자료형을 대조할때는 is를 쓴다.
        continue                             ## continue는 아래 하단의 구문을 실행시키지 않고 다시 반복문 구문으로 돌아간다.
    print("current type:", v, type(v))       ## boolean 타입이 아닌 경우, 자료형이 출력
    print("multiply by 3", v*3)
    print(True * 3)

print()


# [for - else, python에서 독보적인 문법]
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15 , 34, 36, 38]
for num in numbers:                    ## for문에서 반복하는 모든 원소를 전부 다 반복했을 경우에
    if num == 49:                      ## 즉, break문을 실행하지 못하였을때,
        print("Check : 49")            ## 마지막으로 esle문을 수행한다.
        break
else:                                   ## 끝까지 49라는 숫자를 찾아봤지만, 49라는 숫자는 없어
    print('Pass : 49')                  ## else구문이 실행되었다.

print()


# [구구단 출력]
for i in range(2,10):
    for j in range(1,10):
        print('{:4d}'.format(i*j),end='')       ## {:4d}를 통해 _ _ _ _ 칸 자리 생성, format함수를 이용해 mapping, end옵션을 이용해 띄어쓰기
    print()                                     ## 줄바꿈

# [변환 예제]
name2 = 'Aceman'
print('Reversed', reversed(name2))      ## reversed object at 0x000002397DFA7908, 객체의 주소값이 표기된다.
print('List', list(reversed(name2)))    ## List ['n', 'a', 'm', 'e', 'c', 'A']
print('Tuple', tuple(reversed(name2)))  ## Tuple ('n', 'a', 'm', 'e', 'c', 'A')
print('set', set(reversed(name2)))      ## set {'n', 'a', 'A', 'm', 'c', 'e'}, 순서 x, 실행할때마다 위치가 무작위로 바뀐다.
