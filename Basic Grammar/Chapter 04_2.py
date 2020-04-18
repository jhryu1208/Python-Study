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

# [예제 1]
names = ['kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']
for name in names:
    print('You are : ', name)
