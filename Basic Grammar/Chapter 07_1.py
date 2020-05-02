# Chapter07_1
# 파이썬 예외 처리의 이해
# 예외 종류
# SyntaxError      : 문법오류
# TypeError        : 서로 계산할 수 없는 자료형을 계산했을 떄
# NameError        : 없는 변수를 참조할 때
# IndexError, ValueError, KeyError ......
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계)발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다.
# 4. 예외 무시

# [SyntaxError : 문법오류]
## print('error)
## print('error'))
## if True
##      pass

# [NameError : 참조없음]
## a = 10
## b = 15
## print(c)

# [ZeroDivisionError]
## print(100/0)

# [IndexError]
## x = [50, 70, 90]
## print(x[1])
## print(x[4])
## print(x.pop())
## print(x.pop())
## print(x.pop())
## print(x.pop())

# [KeyError]
## dictionary = {'name': 'Ryu', 'Age': 23, 'City': 'Seoul'}
## print(dictionary['hobby'])
## print(dictionary.get('hobby'))  None이 출력됨

# [예외 없는 것을 가정하고 프로그램을 작성 -> 런타임 예외 발생 시 예외 처리 권장(EAFP)]

# [AttributeError]
## 모듈, 클래스에 있는 잘못된 속성 사용 예외
## import time
## print(time.time2())

# [ValueError]
## 어떤 자료구조안에서, 자료를 참조하려고하는데, 존재하지 않을떄 발생
## x = [10, 50, 90]
## x.remove(50)
## print(x)
## x.remove(200) -> Error발생

# [FileNotFoundError]
## f = open('test.xlsx') -> FileNotFoundError: [Errno 2] No such file or directory: 'test.xlsx'

# [TypeError]
## 자료형에 맞지 않는 연산을 수행 할 경우
## x = [1, 2]
## y = (1, 2)
## z = 'test'

## print(x + y) -> TypeError: can only concatenate list (not "tuple") to list
## print(x + z) -> TypeError: can only concatenate list (not "str") to list
## print(y + z) -> TypeError: can only concatenate tuple (not "str") to tuple
## but, 아래와 같이 형변환을 이용하면 가능
## print(x+list(y))
## print(x+list(z))


# [예외 처리 기본]
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1 : 여러개 가능
# excpet 에러명2 :
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

# try구문이 실행될경우 except문이 실행, 실행안될 경우 else구문이 실행

name = ['Ryu','Jin','Kim']

# [예제1]
try:
    z = 'Ryu' ## 'Lee' -> 예외 처리된다.
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x+1))

except ValueError:
    print('Not found it! - Occurred ValueError!')
else:
    print('Ok! else.')

print()


# [예제2]
try:
    z = 'Ryu' ## 'Lee' -> 예외 처리된다.
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x+1))

except Exception:
    ## Exception을 쓰거나 except만 쓸 경우 : 모든에러를 다잡아줌, but 어떤 에러가 발생했는지 정확하게 알 수 없다.
    ## 하지만, 가능한 정확하게 에러명을 기입해주는 것이 좋다.
    print('Not found it! - Occurred ValueError!')
else:
    print('Ok! else.')

print()


# [예제3 - 가장 많이 쓰이는 방법]
try:
    z = 'Lee'           ## 'Lee' -> 예외 처리된다.
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x+1))

except Exception as x:  ## 에러의 내용을 alias를 통해서 출력할 수 있다.
    print(x)            ## 'Lee' is not in list 자동 출력
                        ## Exception을 쓰거나 except만 쓸 경우 : 모든에러를 다잡아줌, but 어떤 에러가 발생했는지 정확하게 알 수 없다.
    print('Not found it! - Occurred ValueError!')
else:
    print('Ok! else.')
finally:                ## finally : 예외가 발생하건 말건 무조건 실행된다!
    print('Ok! finally!')

print()


# [예제4 - 보편적으로 유용한 방법]
# 예외 발생 : raise
# raise 키워드로 예외를 직접 발생 시킬 수 있다.
try:
    a = 'Jin'
    if a == 'Ryu':
        print('Ok! Pass!')
    else:
        raise ValueError    ## Ryu만 접근 가능하게끔, 전부 ValueError처리
except ValueError:
    print('Occurred! Exception!')
else:
    print('Ok! Hello Ryu!')
