# Chapter 03_6
# 집합(Set) 특징
# 집합(Set) : 자료형(순서 x, 중복 x)

# [선언]
a = set()                                   ## 빈집합
b = set([1, 2, 3, 4, 4, 4])                 ## 중복된 값을 넣어도 결과값은 4하나만 나온다
c = set([1, 4, 5, 6])                       ## Set()을 정확하게 list를 이용하여 문법적으로 선언
d = set([1, 2, 'Pen', 'Cap', 'Plate'])      ## Set() 문자형과 정수형 동시에 둘다 삽입가능
e = {'foo', 'bar', 'bazz', 'foo', 'qux'}    ## {}로 선언가능, 딕셔너리에서 Key없이 원소만 나열한다면 Set에 해당한다.
f = [42, 'foo', (1, 2, 3), 3.141592]        ## Set()에는 서로다른 자료형과 튜플 또한 삽입 가능하다.

print('a - ',type(a), a, 2 in a)            ## in 연산자를 사용가능 -> <class 'set'> set() False
print('b - ',type(b), b)                    ## 중복된 데이터는 표시되지 않는다. -> <class 'set'> {1, 2, 3, 4}
print('c - ',type(c), c)
print('d - ',type(d), d)
print('e - ',type(e), e)
print('f - ',type(f), f)

print()


# [튜플 변환 (set -> tuple)]
t = tuple(b)
print('t - ', type(t), t)                   ## t -  <class 'tuple'> (1, 2, 3, 4)
print('t - ', t[0], t[1:3])                 ## t -  1 (2, 3)

print()


# [리스트 변환 (set -> list)]
l = list(c)
l2 = list(e)
print('l - ', l)                            ## l -  [1, 4, 5, 6]
print('l2 - ', l2)                          ## l2 -  ['qux', 'bar', 'foo', 'bazz']

print()


# [길이]
print(len(a))   ## 0
print(len(b))   ## 4
print(len(c))   ## 4
print(len(d))   ## 5
print(len(e))   ## 4
print(len(f))   ## 4

print()


# [집합 자료형 활용]
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 : ', s1 & s2)                ## s1 & s2 -> s1과 s2의 교집합 -> s1 & s2 :  {4, 5, 6}
print('s1 & s2 : ', s1.intersection(s2))    ## A.intersection(B) 연산자를 이용해서 위와 같이 교집합을 구할 수 있다.

print('s1 | s2 : ', s1 | s2)                ## s1 | s2 -> s1과 s2의 합집합 -> s1 | s2 :  {1, 2, 3, 4, 5, 6, 7, 8, 9}
print('s1 | s2 : ', s1.union(s2))           ## A.union(B) 연산자를 이용해서 위와 같이 합집합을 구할 수 있다.

print('s1 - s2 : ', s1 - s2)                ## s1 - s2 -> s1과 s2의 차집합 -> s1 - s2 :  {1, 2, 3}
print('s1 - s2 : ', s1.difference(s2))      ## A.difference(B) 연산자를 이용해서 위와 같이 차집합을 구할 수 있다.

print()


# [중복 원소 확인]
print('s1 & s2 :', s1.isdisjoint(s2))       ## A.isdisjoint(B)  교집합 ㅇ -> False / 교집합 x ->True

print()


# [부분 집합 확인]
print(s1.issubset(s2))                      ## A.issubset(B)  A가 B의 부분집합이니?
print(s2.issubset(s1))                      ## 맞으면 True, 틀리면 False
print(s1.issuperset(s2))                    ## A.issuperset(B) A집합이 B집합을 포함하는가?
                                            ## issuperset 과 issubset은 서로 반대의 기능을한다.
print()


# [데이터 추가&제거]
s1 = set([1, 2, 3, 4])
s1.add(5)           ## Set()은 add() method를 이용해서 자료를 집합 끝에 추가 할 수 있다.
print('s1 - ', s1)

s1.remove(2)        ## set()은 remove() method를 이용해서 자료의 특정 값을 삭제 할 수 있다.
print('s1 - ', s1)

s1.discard(3)       ## set()의 데이터 제거 method에는 discard()도 있다.
print('s1 - ', s1)  ## 하지만, remove를 이용해서 없는값을 제거 하려고하면 오류가 발생하지만,
                    ## discard는 없는 값을 제거하려고해도 오류가 발생하지 않아서 범용성이 높다.

s1.clear()          ## clear()를 이용해 모든 원소 삭제, 빈집합 생성
print('s1 - ', s1)

a = [1, 2, 3]       ## list에서도 clear()를 사용가능
a.clear()
