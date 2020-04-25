# Chapter06_1
# 파이썬 클래스
# OOP(객체 지향 프로그래밍)
# self
# 인스턴스 메소드
# 인스턴스 변수

# [클래스 and 인스턴스 차이 이해]
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재

# [예제1]
# [Class 생성]
## 클래스를 작성하기 위해서는 class키워드를 사용하여 새로운 클래스를 작성한다.
class Dog: # object 상속

    ## pass는 아무것도 수행하지 않는 문법으로 임시로 코드를 작성할 때 사용한다.
    ## pass

    # [클래스 속성 (클래스 변수)]
    ## Dog 클래스에 선언한 species가 클래스 변수이다.
    ## 클래스변수는 클래스안에 함수를 선언하는 것과 마찬가지로 클래스안에 변수를 선언하여 생성한다.
    ## 클래스 변수는 클래스로 만든 모든 객체에 공유된다는 특징이 있다.
    species = 'fisrtdog'


    # [초기화/인스턴스 속성 (인스턴스 변수 - self)]
    ## 클래스 내의 함수는 메소드(Method)라고 부른다.
    ## 일반적인 함수를 만들 때 다음과 같이 작성한다.
    ## def 함수명(매개변수):
    ##      수행할 문장
    ##      ...

    ## __init__메소드 -> 객체를 초기화
    ## __init__ 메서드는 매개변수로 self, name, age 3개의 입력값을 받는다.
    ## 그런데 일반 함수와는 달리 메서드의 첫 번째 매개변수(self)는 특별한 의미를 가진다.
    ## self를 사용하여 클래스 내 멤버에 접근할 수 있다. (C++의 구조체와 유사)
    ## self.Name 라고 쓰면, 인스턴스 변수 Name에 접근할 수 있다.
    ## 객체변수는 다른 객체들에 영향받지 않고 독립적으로 그 값을 유지한다.
    ## 클래스 변수보다는 객체변수를 사용하는 비중이 일반적으로 높다.
    def __init__(self, name, age):
        self.Name = name ## Name과 Age는 속성
        self.Age = age

# 클래스 정보
print(Dog)

# 인스턴스화
## 인스턴스는 코드를 직접구현해서 메모리에 올라간 시점
## 클래스로 만든 객체를 인스턴스라고 한다.
## a = Dog()로 만든 a는 객체이다.
## 그리고 a객체는 Dog의 인스턴스이다.
## 즉, 인스턴스는 특정 객체(a)가 어떤 클래스(Dog)의 객체인지를 관계 위주로 설명할 때 사용한다.
## "a는 객체"
## "a는 Dog의 인스턴스"
## Dog 클래스의 객체를 만드는 방법은 다음과 같다.
a = Dog("mikky", 2)    ## 함수의 재활용이 가능하다.
b = Dog("baby", 3)
c = Dog("mikky", 2)

# 비교
print(a==b, id(a), id(b), id(c))  ## False, id또한 값이 같을지라도 서로다름

# 네임스페이스
print('dog1', a.__dict__)  ## dog1 {'Name': 'mikky', 'Age': 2}
print('dog2', b.__dict__)  ## dog2 {'Name': 'baby', 'Age': 3}

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.Name, a.Age, b.Name, b.Age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.Name, a.Age))

print(Dog.species)  ## 클래스 속성은 클래스로 접근가능
print(a.species)    ## 클래스 속성은 인스턴스 변수로도 접근가능
print(b.species)    ## Therefore, 클래스 속성을 공유한다.

# [예제2]
# self의 이해
class selfTest:
    def func1():
        print('Func1 Called')
    def func2(self):
        print(id(self))
        print('Func2 Called')

f = selfTest()
print(dir(f))
print(id(f))        ## self의 아이디값이랑 동일함 -> self가 f를 받음
## f.func1()        ## 하나의 변수가 들어갈라하지만, 자리가 없어서 error
f.func2()           ## self매개변수가있는 함수를 인스턴스 메소드라 하고, 인스턴스로 접근해서 호출하는 방법이있다.

selfTest.func1()    ## 매개변수가 없는 클래스 메소드는 클래스로 접근하여 호출 가능하다.
## selfTest.func2() ## 하나의 변수를 요구하지만, 변수가 없어서 error
selfTest.func2(f)   ## 요구하는 하나의 변수를 넣어줘서 error가 없음
                    ## 또한, 클래스로 접근하여 인스턴스 메소드를 호출하려면, 인스턴스값을 별개로 대입시켜줘야한다.

                    ## (정리)
                    ## 1. 클래스 메소드 호출법
                    ##  : 클래스명.메소드명()
                    ## 2. 인스턴스 메소드 호출법
                    ##  : 인스턴스명.메소드명()
                    ## or 클래스명,메소드명(인스턴스명)

# [예제3]
# 클래스 변수, 인스턴스 변수
class warehouse:
    ## 클래스 변수
    stock_num = 0 ## 재고

    def __init__(self,name):
        ## 인스턴스 변수
        self.name = name
        warehouse.stock_num += 1 ## 객체가 하나 생성될때마다 1증가

    def __del__(self):
        warehouse.stock_num -= 1 ## 객체가 하나 제거될때마다 1감소

user1 = warehouse('Ryu')    ## 총 2번의 인스턴스화가 진행됨
user2 = warehouse('Jin')

print(warehouse.stock_num)
# warehouse.stock_num = 50
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', warehouse.__dict__)
print('>>>', user1.stock_num)

del user1 ## 인스턴스에서 메모리(객체) 삭제
print('after', warehouse.__dict__)

# [예제4]
class Dog2:
    species = "firstdog"
    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    def info(self):
        return '{} is {} years old'.format(self.Name, self.Age)

    def speak(self, sound):
        return '{} says {}!.'.format(self.Name, sound)

## 인스턴스 생성
c = Dog2('july', 4)
d = Dog2('Marry', 10)
## 메소드 호출
print(c.info())
print(d.info())
## 메소드 호출
print(c.speak('wal wal')) ## sound 변수에 wal wal이라는 인수 전달
print(d.speak('mong mong'))
