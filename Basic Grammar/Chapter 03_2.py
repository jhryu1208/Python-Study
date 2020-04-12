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
