# Chapter 03-3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형 (순서 o, 중복 o, 수정 o, 삭제 o)

# [선언]
a = []
print(type(a))
b = list()
c = [70, 75, 80, 85]                         ## 0 ~ 3 배열
print(len(c))                                ## 0 ~ 3 -> 4칸 -> len 결과 4출력
d = [1000,10000.1,'Ace','Base', 'Captine']   ## 서로 다른 자료형을 리스트에 담을 수 있다.
e = [1000,10000.1, ['Ace','Base','Captine']] ## list안에 list 배치 가능
f = [21.42, 'foobar', 3, 4, False, 3.14159]  ## boolean형을 포함한 다양한 자료형을 담을 수 있다.

print()


# [인덱싱]
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])                         ## 문자열에서와 똑같은 결과로, 뒤에서 부터 -1, 따라서 Captaine 출력
print('e - ', e[-1][1])                      ## e에서 -1은 list이고, list에서 첫번째 indexing을 하기에, Base가 출력
print('e - ', list(e[-1][1]))                ## 리스트 형태로 변환

print()


# [슬라이싱]
print('d - ', d[0:3])                        ## d[0], d[1], d[2] 출력
print('d - ', d[2:])                         ## d[2]부터 끝까지 출력
print('e - ', e[-1][1:3])                    ## e[-1]이므로 list를 indexing하고, 그 list안을 slicing 하여 1, 2번 배열을 출력한다.

print()


# [리스트 연산]
print('>>>>>')
print('c + d', c + d)                        ## c배열과 d배열이 이어진다, c배열이 먼저 선언되어 앞서 출력
print('c*3', c*3)                            ## c배열이 연속3번 이어진다.
##print("'Test' + c[0]", 'Test' + c[0])      ## 문자열 + 정수형과의 합은  error
print("'Test' + c[0]", 'Test' + str(c[0]))   ## 정수형인 c[0]를 문자형으로 형변환하면 정상적으로 합칠수있다.

print()


# [값 비교 ]
print(c==c[:3]+c[3:])
print(c)
print(c[:3])                                 ## c[0]~c[2] 까지 출력
print(c[3:])                                 ## c[3] 출력

print()


# [Identity (id)]
temp = c                                     ## temp와 c는 같은 주소를 참조하고 있다.
print(temp, c)
print(id(temp))
print(id(c))

print()


# [리스트 수정, 삭제]
print('>>>>>')
c[0] = 4
 ## c[0]에 있던 70이 4로 바뀌었다.
print('c -', c)

## c[1:2]는 c[1]을 의미하고, 이때 c[1]을 'a', 'b', 'c'는 원소로서 삽입된다.
## c[1:2] = [['a', 'b', 'c']]  이때는, list ['a', 'b', 'c']가 c[1]대신 삽입된다.
c[1:2] = ['a', 'b', 'c']
## slicing방식이 아닌 index를 지정해서 넣는 경우, 원소로서 들어가는것이아니라, 리스트로서 들어간다.
## **(중첩list)** c[1] = ['a', 'b', 'c'] <=> c[1:2] = [['a', 'b', 'c']]
c[1] = ['a', 'b', 'c']
print('c -', c)

## 위의 결과 값 c - [4, ['a', 'b', 'c'], 'b', 'c', 80, 85] 에서
## c[1],c[2]가 공백으로 바뀐다.
## 따라서, c - [4, 'c', 80, 85]의 결과값을 가진다.
c[1:3]=[]
print('c -', c)

## **삭제**
del c[2]
print('c -', c)

print()


# [리스트 함수]
a = [5, 2, 3, 1, 4]
print('a - ', a)

a.append(10)       ## 배열의 끝에 원소를 추가함
print('a - ', a)

a.sort()           ## 오름차순을로 정렬, 데이터가 많을시 긴 처리시간
print('a - ', a)

a.reverse()        ## 역순으로 정렬, 데이터가 많을시 긴 처리시간
print('a - ', a)

print('a - ', a.index(3), a[3])  ## 해당 인덱스의 자료를 가져오는 방법 : index(위치)
print('a - ', a.index(3))   ## a -  2

a.insert(2, 7)     ## 자료사이에 값을 집어넣는 방법 : insert(위치, 추가할 값)
print('a - ', a)

a.reverse()
print('a - ', a)

a.remove(10)       ## 데이터 갯수가 많을 시, 불필요한 특정 데이터를 제거하는 방법 : remove(제거할 값)
print('a - ', a)

print('a - ', a.pop())  ## 마지막 index에 해당하는 원소를 출력하고,
print('a - ', a)        ## 나머지 원소들로 리스트를 다시 구성하는 방법 : 리스트.pop()
print('a - ', a.pop())
print('a - ', a)

print('a - ', a.count(4))   ## 찾는 특정 값의 중복된 갯수 구하는 방법 : 리스트.count(값)

ex = [8,9]
a.extend(ex)    ## 끝부분에 리스트 추가
print('a - ', a)

## 삭제 : remove, (알고리즘에서 중요!!) pop, del

# [반복문 활용]
while a:
    data = a.pop()
    print(data)
