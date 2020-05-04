# Chapter8_2
# 파이썬 외장(External) 함수
# 실제 프로그램 개발 중 자주 사용
# 종류 : sys, pickle, shutil, temfile, time, random 등

# [예제1]
import sys
print(sys.argv)

# [예제2, 강제 종료]
# sys.exit()

# [예제3, 파이썬 패키지 위치]
print(sys.path)

# [pickle : 객체 파일 읽기, 쓰기]
import pickle

# [예제4, 쓰기]
## 파일을 출력할때는 wb라고 써야하며, 이는 테스트 파일 입출력과 공통적인 특징이다.
f = open("test.obj", 'wb')      ## w = write, b = binary    ## f를 open

obj = {1:'python', 2:'study', 3:'basic'}
pickle.dump(obj, f)             ## 쓸때는 dump, 값을 전달(파일 출력)해주는 dump 메서드
f.close()                                                   ## f를 close, 사용이 끝났으면 반드시 close시켜줘야 한다.

# [예제5, 읽기]
f = open('test.obj', 'rb')      ## r = read, b = binary
data = pickle.load(f)           ## 읽을때는 load
print(data, type(data))
f.close()

# [os : 환경변수, 디렉토리(파일) 처리 관련, 운영체제 직업 관련]
# mkdir, rmdir(비어 있으면 삭제), rename
# [예제6]
import os
print(os.environ)               ## 사용자의 pc정보를 튜플형태로 보여줌
print(os.environ["USERNAME"])
print(os.environ["ATOM_HOME"])

# [예제7(현재경로)]
print(os.getcwd())              ## 현재 실행파일의 경로를 볼 수 있음

# [time : 시간 관련 처리]
import time
# [예제8]
print(time.time())                  ## 1588555518.3012598, 시간이 숫자로 출력된다. 현재 시간, 시분초, 밀리세컨 등등...

# [예제9, 형태 변환]
print(time.localtime(time.time()))  ## time.struct_time(tm_year=2020, tm_mon=5, tm_mday=4, tm_hour=10, tm_min=25, tm_sec=18, tm_wday=0, tm_yday=125, tm_isdst=0)
                                    ## time()함수에서 표현된 현재시간을 분해해서 보여준다. 2020년 5월 4일 10시 25분 18초

# [예제10, 간단 표현]
print(time.ctime())                 ## Mon May  4 10:26:32 2020

# [예제11, 형식 표현]
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))      ## 2020-05-04 10:28:13, %Y-%m-%d %H:%M:%S 대문자 소문자 구별 유의

# [예제12, 시간 간격 발생]
for i in range(5):
    print(i)
    # time.sleep(1)       ## sleep(x) 의 x는 초(sec)가 들어간다. 1초간격으로 쉬면서, for구문이 실행되는 것을 확인 할 수 있다.

# [random : 난수 리턴]
import random

# [예제 13]
print(random.random())          ## 0 ~ 1 사이의 실수가 랜덤하게 출력된다.

# [예제 14]
print(random.randint(1, 45))    ## 1부터 45 사이의 int값을 랜덤하게 출력한다.
print(random.randrange(1, 45))  ## 1부터 44(45-1) 사이의 int값을 랜덤하게 출력한다.

# [예제 15, shuffle]
d = [1, 2, 3, 4, 5]
random.shuffle(d)               ## list의 배열들이 suffle 된다.
print(d)

# [예제16, 무작위 선택]
c = random. choice(d)           ## list안의 숫자들이 임의로 choice된다.
print(c)

# webbrowser : 본인 os의 웹 브라우저 실행
import webbrowser
webbrowser.open("www.google.com")
webbrowser.open_new("www.google.com")
