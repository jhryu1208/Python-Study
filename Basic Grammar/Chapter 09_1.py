# Chapter 09_1
# 파일 읽기 및 쓰기

# *읽기 모드 : r, *쓰기모드 : w, *추가모드 : a, 텍스트 모드 : t, 바이너리 모드 : b
# 상대 경로(' ../ , ./'), 절대 경로 ('C:\Django\exapmle..')

#  [파일 읽기 (Read)]
#  [예제1]
## 절대경로
## f = open('F:\\Programming\\Python\\Python-Basic\\Basic Grammar\\resource\\it_news.txt', 'r', encoding='UTF-8')
## 상대경로
f = open('./resource/it_news.txt', 'r', encoding='UTF-8')

## 속성확인
print(dir(f))
## 인코딩 확인
print(f.encoding)
## 파일 이름
print(f.name)
## 모드 확인
print(f.mode)
cts = f.read()
print(cts)
## 반드시 open한 파일은 close
f.close()

# [예제2]
## 많이 사용되는 방법
## with문을 사용하 close함수를 사용하지 않아도 단락에서 벗어나면 자동으로 닫아준다.
## with문을 벗어나면 다른 코드가 실행된다는 의미로도 볼 수 있다.
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

# [예제3]
# read() : 전체 읽기, read(10) : 10Byte
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)        ## Right now gamers can
    c = f.read(20)
    print(c)        ## pay just $1 for acc
    c = f.read(20)
    print(c)        ## ess to hundreds of t -> 커서(이어서 읽기)가 내부적으로 동작함을 확인 할 수 있다.
    f.seek(0,0)     ## seek을 통해 처음부터 읽기 시작이 가능하다. (초기화)
    c = f.read(20)  ## Right now gamers can
    print(c)

print()

# [예제4]
# readline : 한 줄 씩 읽기
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)     ## Right now gamers can pay just $1 for access to hundreds of titles across PC  -> 첫번째 줄을 읽어옴
    line = f.readline()
    print(line)     ## and Xbox via Microsoft Xbox Game Pass Ultimate service?but dont  -> 두번째 줄을 읽어줌

print()

# [예제5]
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    ## 줄바꿈 기준으로 list가 형성되었다.
    ## ['Right now gamers can pay just $1 for access to hundreds of titles across PC \n',
    ##  'and Xbox via Microsoft Xbox Game Pass Ultimate service?but dont \n',
    ##  'activate that insanely cheap one-month trial just yet. You can lock in up to \n',
    ##  'three years of Xbox Game Pass Ultimate with that same dollar if you play \n',
    ##  'your cards right.\n',
    ##  '\n',
    ##  'When you activate Microsoft��s E3 2019 promotion, it not only begins the trial, \n',
    ##  'but also converts existing Xbox Live Gold and standard Xbox Game Pass \n',
    ##  'subscriptions on your account to Game Pass Ultimate (normally $15 per \n',
    ##  'month). Any prepaid time up to the maximum of three years gets the upgrade.\n',
    ##   '\n']
    print()
    for c in cts:
        print(c, end='')

print()

# [파일 쓰기 (Read)]

# [예제1]
## atom이 관리자권한으로 실행되어야 정상적으로 쓰기가 가능하다.
with open('./resource/contents1.txt', 'w') as f:
    f.write('I love python\n')

# [예제2]
## 문장을 이어서 추가하고 싶을 경우, 위의 예제1을 반복하게되면 처음에 작성한 문장에 덮어쓰기가 된다.
## 따라서 append, 즉 'a' 를 이용하여 문장 추가가 가능하다.
with open('./resource/contents1.txt', 'a') as f:
    f.write('I love python2\n')

# [예제3]
# wirtelines : 리스트 -> 파일
with open('./resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

# [예제4]
# file 옵션
## 콘솔에서 print 출력을 확인하는 것이아니라, 연결한 파일을 통해 직접 출력하는 방법
with open('./resource/contents3.txt', 'w') as f:
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
