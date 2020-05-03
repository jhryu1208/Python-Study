# Chapter 08_1
# 파이썬 내장(Built-in) 함수
# 자주 사용하는 함수 위주로 실습
# 사용하다보면 자연스럽게 숙달가능
# str(), int(), tuple() 형변환은 이미 학습

# [1. abs() 절대값]
print(abs(-3))

# [2. all() : iterable 요소를 검사 (참, 거짓), &와 유사]
## all안에 있는 요소들이 모두 참이어야 true가 나온다.
## 하나라도 0이 있을경우, 또는 빈문자열이 있을경우 false를 출력한다.
print(all([1, 2, 3]))       ## True
print(all([1, 2, 0]))       ## False
print(all([1, 2, '']))      ## False

# [3. any(), or와 유사]
## any안에 있는 요소가 하나라도 참인 값이 있을경우 True가 나온다.
## any안에 있는 요소들이 모두 거짓인 값일 경우 False가 나온다.
print(any([1, 2, 3]))       ## True
print(any([1, 2, 0]))       ## True
print(any([1, 2, '']))      ## True
print(any([0, 0, 0]))       ## False

# [4. chr : 아스키코드 -> 문자, 5. ord : 문자 -> 아스키]
print(chr(44))      ## ,
print(chr(65))      ## A
print(ord(','))     ## 44
print(ord('A'))     ## 65

# [6. (중요)enumerate : 인덱스 + Iterable 객체 생성]
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i, name)
    ## 0 abc
    ## 1 bcd
    ## 2 efg

# [7. (중요)filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출]
def conv_pos(x):
    return abs(x) > 2

## 함수호출 (conv_pos())을 써줄 필요없고 함수이름(conv_pos)만 안에 적어주면된다.
## filter함수내에서 함수이름만적어도 알아서 호출해 주기 때문에 가능하다.
print(filter(conv_pos, [-3, -2, 0, -5, 6]))                     ## <filter object at 0x0000020EFC379CC8>
print(list(filter(conv_pos, [-3, -2, 0, -5, 6])))               ## 위의 값을 형변환 하면, [-3, -5, 6]
print(list(filter(lambda x : abs(x) > 2, [-3, -2, 0, -5, 6])))  ## filter함수 내부에서 lambda를 이용하여 왼쪽과 같이 나타낼 수 있다.

# [8. id : 객체의 주소값 (래퍼런스) 반환]
print(id(int(5)))   ## 140725922200768
print(id(int(4)))   ## 140725922200736

# [9. len : 요소의 길이 반환]
print(len('abcdefg'))
print(len([1, 2, 3, 4, 5, 6, 7]))

# [10. max, min : 최대값과 최소값]
print(max([1, 2, 3, 4, 6]))
print(max('Python Study'))      ## y
print(min([1, 2, 3, 4, 6]))
print(min('Python Study'))      ## ' '

# [11. (중요)map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출]
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs, [1, -3, 2, 0, -5, 6])))  ## 모든값들이 적용
print(list(map(lambda x: abs(x), [1, -3, 2, 0, -5 ,6])))

# [12. pow : 제곱값을 반환]
print(pow(2,10))

# [13. range : 반복가능한 객체(Iterable)반환]
print(range(1,10, 2))         ## range(1, 10, 2)
print(list(range(1,10, 2)))   ## [1, 3, 5, 7, 9]
print(list(range(0,-15, -1))) ## [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14]

# [14. round : 반올림]
print(round(3.141592))    ## 소수 첫째 자리에서 반올림
print(round(3.141592, 2)) ## 소수 둘째 자리에서 반올림

# [15. sorted : 반복가능한 객체(Iterable)를 정렬 후 반환]
print(sorted([6, 7, 4, 3, 2, 1])) ## 오름차순 정렬 : [1, 2, 3, 4, 6, 7]
a = 'python'
print(sorted(list(a)))            ## 알파뱃 순서대로 오름차순 정렬 : ['h', 'n', 'o', 'p', 't', 'y']

# [16. sum : 반복가능한 객체(Iterable) 합 반환]
print(sum([6, 7, 8, 9, 10]))      ## 40
print(sum(range(1,101)))          ## 1부터 100까지의 합 5050

# [17. type : 자료형]
print(type(3))      ## <class 'int'>
print(type({}))     ## <class 'dict'>
print(type(()))     ## <class 'tuple'>
print(type([]))     ## <class 'list'>

# [18. zip : 반복가능한 객체(iterable)의 요소를 묶어서 반환]
a = [10, 20, 30]
b = [40, 50, 60]
c = [70, 80]
print(zip(a, b))                ## <zip object at 0x0000021786CC3CC8>
print(list(zip(a, b)))          ## [(10, 40), (20, 50), (30, 60)]
print(list(zip(a, c)))          ## 짝이 안맞는 경우, [(10, 70), (20, 80)]
print(type(list(zip(a, b))[0])) ## 리스트의 0번쨰인 (10, 40)은 튜플, <class 'tuple'>
