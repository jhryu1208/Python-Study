# Chapter 03_5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형 (순서 x, 키 중복 x, 수정 o, 삭제 o)

# [선언]
a = {'name': 'Kim', 'phone': '01033337777', 'birth': '870514'}  ## Key와 Value로 이루어져있다.
b = {0 : 'Hello Python'}    ## Key는 정수형으로도 선언할 수 있다. 대부분은 문자형
c = {'arr':[1, 2, 3, 4, 5]} ## Value로 list가 들어 갈 수 있다.

d = {                       ## 왼쪽과 같이 괄호를 사용하여도 선언 가능하다.
    'Name': 'Jihyun',
    'City': 'Seoul',
    'Age' : 23,
    'Grade': 'A',
    'Status': True
}

e = dict([                  ## 자주 쓰이는 형태는 아니지만,
    ('Name', 'Jihyun'),     ## dict안에 list안의 tuple을 사용해 선언 할 수 있다.
    ('City', 'Seoul'),      ## 튜플을 사용했기에 :가 아닌 ,를 사용한다.
    ('Age', 23),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict(                   ## 위보다 더 간단한게 왼쪽과같이 표현 가능
    Name = 'jihyun',
    city = 'Seoul',
    Age = 23,
    Grade = 'A',
    Status = True
)

print('a - ',type(a), a)
print('b - ',type(b), b)
print('c - ',type(c), c)
print('d - ',type(d), d)
print('e - ',type(e), e)
print('f - ',type(f), f)

print()


# [출력]
print('a - ', a['name'])        ## a의 'name'을 가져와라 -> Kim
print('a - ', a.get('name'))    ## get()함수를 이용해서도 위와 같이 할 수 있다.
print('b - ', b[0])             ## 하지만, 첫번쨰 방법은 Key가 없을시 에러가 뜨지만,
print('b - ', b.get(0))         ## get()함수를 이용한 방법은 에러가 뜨지않고 None이 발생한다.
print('f - ', f.get('city'))    ## 따라서, 첫번째 방법보다는 두번쨰 방법이 더 유용하다.
print('f - ', f.get('Age'))

print()


# [딕셔너리 추가]
a['address'] ='seoul'           ## address라는 Key가 생기고
print('a - ',a)                 ## 그에 대한 값으로 seoul이 추가됨
a['rank'] = [1, 2, 3]           ## rank라는 key가 생기고
print('a - ', a)                ## 그에 대한 값으로 list [1, 2, 3]이 추가됨

print()


# [딕셔너리 길이 (키의 개수)]
print('a -', len(a))            ## a의 키의 개수는 차후에 2개 추가되었으므로, 5
print('b -', len(b))            ## b의 키의 개수는 1
print('c -', len(c))            ## c의 키의 개수는 1
print('d -', len(d))            ## d의 키의 개수는 5

print()


# dict_keys, dict_values, dict_items : 반복문에서(__iter__) 사용 가능
# [keys, values, items]
print('a - ', a.keys())  ## Key만 가져오고, Value는 가져오지 않는다.
print('b - ', b.keys())  ## 결과값 : dict_keys([Key1, Key2, Key3])
print('c - ', c.keys())
print('d - ', d.keys())

print('a - ', list(a.keys()))   ## keys로 출력된 값들을
print('b - ', list(b.keys()))   ## list로 형변환해서 출력

print()

print('a - ', a.values()) ## Value만 가져오고, Key는 가져오지 않는다.
print('b - ', b.values()) ## 결과값 : dict_values([Value1, Value2, Value3])

print('a - ', list(a.values()))   ## values로 출력된 값들을
print('b - ', list(b.values()))   ## list로 형변환해서 출력

print()

print('a - ', a.items())  ## Key와 Value 모두 가져온다.
print('b - ', b.items())  ## 결과값 : dict_items([(Key1, Value1), (Key2, Value2), (Key3, Value3)])
print('c - ', c.items())  ## Key 와 Value가 튜플로 묶여 연속된 list의 형태를 보인다.

print('a - ', list(a.items()))  ## items로 출력된 값들을
print('b - ', list(b.items()))  ## list로 형변환해서 출력
print('c - ', list(c.items()))

print()


# [pop, popitem]
print('a - ', a.pop('name'))  ## name이라는 Key와 Value를 호출하고 삭제
print('a - ', a)

print('c - ', c.pop('arr'))   ## arr이라는 Key와 Value를 호출하고 삭제
print('c - ', c)

print()

print('f - ', f.popitem())    ## 랜덤한 key와 value를 호출하고 삭제
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())    ## 결국엔 key와 value 모두를 랜덤한 순서대로 삭제함
print('f - ', f)

print()


# [유무 여부 판별]
print('a - ', 'birth' in a)   ## 'y' in x : x라는 딕셔너리에 y라는 Key가 있니?
print('d - ', 'City' in d)    ## 있으면 True, 없으면 False

print()


# [수정 & 추가]
a['test'] = 'test_dict'     ## 추가
print('a - ', a)

a['address'] = 'Daejeon'    ## 수정
print('a - ', a)            ## 왼쪽과 같이해도 수정이 가능하지만, method를 이용한 방법이 존재한다.

a.update(birth='971208')    ## 수정 method 인 update
print('a - ', a)            ## .update(Key ='수정value')

temp={'address': 'Busan'}   ## 명시적인 방법으로도 수정가능
a.update(temp)
print('a - ', a)
