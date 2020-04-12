# Chpater 03_2
# 파이썬 기초
# (중요)문자형

# [문자열 생성]
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))

## len : 공백포함 문자열의 길이를 측정
print(len(str1), len(str2), len(str3), len(str4))

print()


# [빈문자열]
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# [이스케이프 문자 사용]
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : \ 문자
\' : ' 문자
\" : " 문자
\0 : 널 문자

"""
## 큰따옴표는 '와 상관없이 괜찮지만,
print("I'm boy")
## 작은 따옴표를 이용하여 아래와 같이 출력하면 '때문에 에러가 뜬다.
## print('I'm boy')
## \ : 뒤에있는 특수기호를 있는 그대로 표시
print('I\'m boy')
print('I\\m boy')
print('a\tb')
print('a\"\"b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)

escape_str2 = 'What\'s on TV?'
print(escape_str2)

## 탭, 줄 바꿈
t_s1 = "Click\tStrat!"
t_s2 = "New Line \nCheck!"
print(t_s1)
print(t_s2)

## Row String
## 문자열앞에 r만 붙여주면된다.
## 있는 그대로 표시해준다 \의 기능을 무시한다
## \t \n 포함 무시한다.
## 드라이브의 경로를 표시할때 자주 사용한다.
raw_s1 = r'D:\python\test'
print(raw_s1)

# [멀티라인 입력]
multi_str1="""
String
Multi line
Test
"""
print(multi_str1)

## 또는 \를 이용해서 아래와 같이 깔끔하게 쓸수있다.
multi_str2 = \
"""
String
Multi line
Test
"""

print(multi_str2)

print()


# [문자열 연산]
str_o1="Python"
str_o2="Apple"
str_o3="How are you doing"
str_o4="Seoul Deajeon Busan Jinju"

## 문자열이 3번 반복되서 출력된다
print(str_o1*3)
## 서로 다른 문자열이 이어져 출력된다.
print(str_o1+str_o2)
## y라는 문자열이 str_o1에 있니?, 있으면 True, 없으면 False
print('y' in str_o1)
print('n' in str_o1)
## P라는 문자열이 str_o2에 있니?, 없으면  True, 있으면 False
print('P' not in str_o2)

print()


# [문자열 형 변환]
## str()을 이용하여 정수형,bool형 데이터를 문자열 데이터로 형변환 하였다.
print(str(66),type(str(66)))
print(str(10.1),type(str(10.1)))
print(str(True),type(str(True)))

print()


# [문자열 함수]
## 대부분의 문자열관련 함수들은 구글링해서 나오므로, 필요시 즉각 찾으면된다.
## capitalize()함수는 첫번쨰 단어의 앞글자를 대문자로 바꿔준다.
print("Capitalize : ", str_o1.capitalize())

## endswith()함수는 마지막 문자가 무엇인지 체크할떄 사용한다.
## 마지막에 해당하면 True, 아니면 False
print("endswith : ", str_o2.endswith("s"))
print("endswith : ", str_o2.endswith("e"))

## replace("x","y")는 글자에서 x에 해당하는 문자를 y로 바꿔준다.
## (띄어쓰기 포함)
print("replace : ",str_o1.replace("thon"," Good"))

## sorted()함수는 문자열을 입력받아서 기준에 맞게 정렬해서 리스트형태로 반환한다.
print("sorted : ",sorted(str_o1))

## split()함수는 문자열을 단어 단위 또는 문장 단위 기준으로 분리할떄 사용.
print("split : ", str_o4.split(' '))

# [반복(시퀀스)]
im_str = "Good Boy!"

## '__iter__' 라는 class가 im_str안에서 dir을통해 검색됨
## 이때 '__iter__'가 반복이 가능하다는 의미이다.
print(dir(im_str))

## 반복
for i in im_str:
    print(i)
