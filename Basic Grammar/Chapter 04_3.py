# Chapter 04_3
# 파이썬 반복문
# while 실습

# while <expr>:
#    <statement(s)>

# [예제 1]
n = 5
while n > 0:
    n = n - 1
    print(n)

print()


# [예제 2]
a = ['foo', 'bar', 'baz']
while a:            # while a는 while True와 같은 의미
    print(a.pop())

print()


# [if 중첩. 예제 3]
# break, conitnue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended')

print()

m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Ended')


# [if 중첩. 예제 5]
i = 1
while i <= 10:
    print('i : ', i)
    if i == 6:
        break
    i += 1

# [while - else 구문. 예제 6]
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:                   ## break를 거치지 않는다면, else구문이 실행됨
    print('else out')

print()


# [예제 7]
a = ['foo', 'bar', 'baz', 'qux']
s = 'qux'

i = 0

while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'not found in list')

print()


# [무한반복]
# while True:
#   print('Ryu')

print()


# [예제 8]
a = ['foo', 'bar', 'baz']

while True:
    if not a:      ## 빈리스트가 되기전에 a는 True이므로 not a는 False 이다. 따라서 break문은 실행되지 않는다.
        break      ## 하지만, 빈리스트가 되면 a는 False이므로 not a는 True이다. 따라서 break문이 실행된다.
    print(a.pop())
