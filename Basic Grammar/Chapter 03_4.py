# Chapter 03-4
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형 (순서 o, 중복 o, 수정 x, 삭제 x) -> 불변 : 한번선언후 끝까지 사용
# 튜플에는 보통 절대 수정될 일없는, 또는 매우 중요한 자료가 저장됨

# [선언]
a = ()
b = (1)                 ## 원소가 하나일때 컴마를 찍지 않으면
print(type(a),type(b))  ## tuple이 아니라 다른 자료형으로 본다.

b = (1,)                ## 원소가 하나일때라도 컴마를 찍어야
print(type(a),type(b))  ## tuple이라 인식한다.

c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')    ## list와 마찬가지로 다른 자료형과 동시사용 가능
e = (100, 1000, ('Ace', 'Base', 'Captine'))  ## list와 마찬가지로 중첩가능

print()


# [인덱싱]
print('>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])  ## tuple또한, list처럼 사칙연산이 가능하다.
print('d - ', d[-1])               ## list와 마찬가지로, -1은 튜플의 끝값
print('d - ', e[-1][1])            ## list와 동일
print('d - ',list(e[-1][1]))       ## list와 동일

print()


# [수정x]
## d[0]=1500 으로 list와 똑같이 수정하려고하면, 에러가 발생한다.

# [슬라이싱]
print('>>>>>')
print('d - ', d[0:3])    ## d -  (100, 1000, 'Ace')
print('d - ', d[2:])     ## d -  ('Ace', 'Base', 'Captine')
print('d - ', d[:2])     ## d -  (100, 1000)
print('d - ', e[2][1:3]) ## d -  ('Base', 'Captine')

print()


# [튜플 연산]
print('>>>>>')
print('c+d', c+d)  ## c+d (11, 12, 13, 14, 100, 1000, 'Ace', 'Base', 'Captine')
print('c*3', c*3)  ## c*3 (11, 12, 13, 14, 11, 12, 13, 14, 11, 12, 13, 14)

print()


# [튜플 함수]
a = (5, 2, 3, 1, 4)
print('a - ', a)            ## a -  (5, 2, 3, 1, 4)
print('a - ', a.index(3))   ## 해당 원소의 index값을 반환해줌, a -  2
print('a - ', a.count(2))   ## 해당 원소의 갯수를 반환해줌, a -  1

print()


# [팩킹 & 언팩킹 (Packing & Unpacking)]

# **[팩킹]
t = ('foo', 'bar', 'baz', 'qux')  ## 하나로 묶음(튜플과 같다)
print(t[0])
print(t[-1])

print()

# **[언팩킹]

(x1, x2, x3, x4) = t   ## ()가 없더라도 성립됨    ## 묶여 있던 원소들을
print(type(x1), type(x2), type(x3), type(x4))   ## 각각의 순서에 따라
print(x1, x2, x3, x4)                           ## 원소가 각각의 변수로 할당되는

print()

# [팩킹 & 언팩킹]
t2 = 1, 2, 3           ## **()가 없어도 튜플 성립**
t3 = 4,
x1, x2, x3 = t2        ## Unpacking
x4, x5, x6 = (4, 5, 6) ## 원소 할당

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
