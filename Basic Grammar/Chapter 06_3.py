# Chapter 06_3
# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분활 된 개별적인 모듈로 구성
# __init__.py : python 3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천
# 상대경로 : ..(부모 디렉토리), .(현재 디렉토리) -> 모듈 내부에서만 사용

# [예제1]
import sub.sub1.module1 ## sub패키지 안에 sub1 이라는 패키지 안에 모여있 많은 모듈들 중에서, module1을 갖고 온다.
import sub.sub2.module2

# [사용]
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()

# [예제2, 패키지 경로가 너무 긴 경우, 추천]
## 사용하고 싶은 특정 모듈을 선택하여 간단하게 패키지를 사용가능한 방법
from sub.sub1 import module1
from sub.sub2 import module2 as m2 ## as : alias

## 위의 경우 패키지 경로가 너무 길떄
## 사용시 일일이 디렉토리를 적어줘야하는 불편함이 있다.
## 이때, from 패키지경로 import 모듈 구문을 사용하면
## 아래와 같이 짧게 모듈을 호출하여 사용할 수 있다.
module1.mod1_test1()
module1.mod1_test2()

## alias(as)를 두고 호출하면 더욱 간단하게 호출이 가능하다.
m2.mod2_test1()
m2.mod2_test2()

print()
print()
print()

# [예제 3, 비추천]
## *로 import하면 하위에있는 모든 파일에 접근할 수 있다.
## 하지만, 수천개의 하위파일이 있을 때, 전부사용하지 않는다면,
## 메모리를 낭비하기에 비추천하는 방법이다.
from sub.sub1 import *
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2()


# [예제4]
import sub.Test.Test1
print(sub.Test.Test1.add(3, 2))

from sub.Test import Test1
print(Test1.power(3,2))

from sub.Test import Test1 as operation
print(int(operation.div(10,5)))
print(type(operation.div(10,5)))

from sub.Test import *
print(Test1.multi(3,2))
