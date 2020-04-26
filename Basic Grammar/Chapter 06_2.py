# Chapter6_2
# 파이썬 모듈
# Module : 함수, 변수, 클래스 등 파이썬 구성요소 등을 모아놓은 파일

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multi(x, y):
    return x * y

def div(x, y):
    return x / y

def power(x, y):
    return x ** y


# print('-'*15)
# print('Called Inner!')
# print(add(5,5))
# print(sub(15,5))
# print(multi(5,5))
# print(div(10,2))
# print(power(5,3))
# print('-'*15)

# [__name__ 사용]
if __name__ == "__main__"       ## 모듈은 사용자입장에서 외부이므로,
print('-'*15)                   ## 사용자입장에서 쓰는 main파일에서는 모듈의 테스트 출력이 진행되지 않는다.
print('Called __main__')
print(add(5,5))
print(sub(15,5))
print(multi(5,5))
print(div(10,2))
print(power(5,3))
print('-'*15)


# [CMD] Module 실습

# >>> import sys                 ## sys 모듈 : 파이썬 인터프리터를 제어할 수 있는 방법 제공
                                 ##            import문을 만날 경우, 파이썬은 다음과 같은 순서대로 모듈 파일을 찾아 나선다.
                                 ##            1. 현재 디렉토리 -> 2. 환경변수 pythonpath에 지정된 경로 -> python이 설치된 경로 및 그 밑의 라이브러리 경로

# >>> print(sys.path)            ## 위의 경로들을 모두 취합하여 sys.path에 리스트 형태로 저장된다.
# >>> print(type(sys.path))      ## sys.path의 type은 실제로 list가 출력된다.
# <class 'list'>

# >>> sys.path.append('F:/math') ## 모듈 경로 삽입
# >>> print(sys.path)
# ['', 'C:/~', ..., 'F:/math']   ## 삽입결과 맨뒤에 F:/math가 추가됨을 확인 할 수 있다.

# >>> import test_module         ## 모듈 불러오기
# ---------------                ## 실행결과
# Called Inner!
# 10
# 10
# 25
# 5.0
# 125
# ---------------

# >>> print(test_module.power(10,3))  ## 모듈 실행하기
# 1000
