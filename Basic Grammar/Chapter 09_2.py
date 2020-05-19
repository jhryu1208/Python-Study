# Chapter 09_2
# CSV 파일 읽기 및 쓰기

# CSV : MEME - text/csv

import csv      ## import로 csv 파일 관련 처리를 도와주 csv패키지

# [예제1]
with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f)
    ## Header Skip
    next(reader)

    ## 객체확인
    print(reader)
    ## 타입확인
    print(type(reader))
    ## 속성 확인
    print(dir(reader)) ## __iter__ ㅇ
    print()

    for c in reader:
        ## print(c)
        ## 타입확인 (리스트)
        ## print(type(c))
        ## list to str (리스트를 문자열로 바꿈)
        print(' : '.join(c))

# [예제2]
with open('./resource/test2.csv', 'r') as f:
    ## delimiter = '구분자' : 구분자를 기준으로 리스트를 배치한다. 잘못된 구분자가 사용되면 scv의 문자를 그대로 가져온다.
    ## ex) "Korea| Democratic People's Republic of"|KP  의경우
    ##     해당 구분자가 아닌 ,로 사용하면 ["Korea| Democratic People's Republic of|KP"] 처럼 덩어리로 리스트화 된다.
    ##     하지만 해당 구분자인 |로 사용하면 ["Korea| Democratic People's Republic of", 'KP'] 처럼 구분자를 기준으로 리스트 객체가 지정된다.
    reader = csv.reader(f, delimiter='|')

    for c in reader:
        print(c)

# [예제3]
with open('./resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f) ## dictionary 형태로 값을 reader에 저장
    ## 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:             ## reader에 저장된 key와 value가 c에 들어감
        for k,v in c.items():    ## c.item을 통해 c의 key와 value값을 모두 가져오고 각 값을 k와 v에서 받는다.
            print(k,v)
        print('==============================================')


# [예제4]
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]]

with open('./resource/write1.csv', 'w', encoding='UTF-8') as f:
    print(dir(csv))
    wt = csv.writer(f)

    ## dir 확인
    print(dir(wt))
    ## 타입 확인
    print(type(wt))

    for v in w:  ## for문 7번 반복, 리스트안의 하나의 리스트는 하나의 레코드로 취급한다
        wt.writerow(v)

# [예제5]
with open('./resource/write2.csv', 'w', encoding='UTF-8') as f:
    ## 필드명
    fileds = ['One', 'Two', 'Three']

    ## Dict writer
    wt = csv.DictWriter(f, fieldnames=fileds)   ## fileds의 One, Two, Three가 fieldnames으로 알아서 들어감.

    ## Header writer
    wt.writeheader()    ##  filednames에서 받은 헤더이름이 암묵적으로 작성된 상태가 된다.

    for v in w:
        wt.writerow({'One' : v[0], 'Two' : v[1], 'Three' : v[2]})
