# Chapter05_1
# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(Lambda)

# 함수정의 방법
# def function_name(parameter):
#     code

# [예제 1]
def first_func(w):      ## 함수 선언
    print("Hello, ", w)

word = "Goodboy"
first_func(word)        ## 함수 호출    ## 괄호 중요!!

print()

# [예제 2]
def return_func(w1):
    value = "Hello, " + str(w1)
    return value

x = return_func('Goodboy2')
print(x)

print()

# [예제 3 (다중반환)]
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3   ## 여러개의 반환값을 반환 할 수 있다.

x, y, z = func_mul(10)  ## unpacking

print(x, y, z)

print()

# [튜플 리턴]
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return(y1, y2, y3)      ## tuple형태로 반환

q = func_mul2(20)           ## unpacking, q는 tuple형태의 반환값을 받았다.
print(type(q), q, list(q))  ## q의 타입은 tuple이며, 형변환 또한 가능하다.

print()

# [리스트 리턴]
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]     ## list형태로 반환

p = func_mul3(30)           ## unpacking, p는 list형태의 반환값을 받았다.
print(type(p), p, set(p))   ## p의 타입은 list이며, 형변환 또한 가능하다.

print()

# [딕셔너리 리턴]
def  func_mul4(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1' : y1, 'v2' : y2, 'v3' : y3}    ## dictionary 형태로 변환

d = func_mul4(40)
print(  type(d),        ## d의 타입은 dictionary
        d,              ## d의 dictionary가 출력됨
        d.get('v1'),    ## get()함수를 이용해 key인 'v1'의 value를 출력할 수 있다. ps) d.['v1']으로도 가져올 수 있지만, 딕셔너리에 포함되지 않은 키일 경우, error가 발생한다. (get의 경우는 발생x)
        d.items(),      ## 복습)  key와 value 모두 가져온다.
        d.keys()    )   ## 복습)  key만 가져오고, Value는 가져오지 않는다.

print()

# [**중요**]
# *args, **kwargs (변수명은자유)
# [*args(언팩킹), *가 붙은게 중요..., 유사 Tuple]
def args_func(*args):                       ## *parameter는 해당 매개변수가 가변이라는 의미 (1개를 받을수도있고 10개를 받을 수도 있고...) ## arg = (Ryu, ...) 인 tuple을 만든다 생각하면 됨
    for i, v in enumerate(args):            ## enumerate(parameter) : 배열에 숫자를 부여하는 함수. ex) 'Lee' -> (0, R), (1, y), (2, u)
        print('Result : {}'.format(i), v)   ## 위 라인에서 unpacking에의해 (순서 -> i), (글자 -> v)
    print('-----')

args_func('Ryu')                            ## Ryu는 *args에 의해 튜플의 원소로 들어가고, 함수내에서 unpacking된다. ex) arg = [R, y, u]가 아니라 arg = [Ryu]
args_func('Ryu', 'Park')                    ## *을 붙이므로써, args는 ('Ryu', 'Park')라는 튜플을 가지게되고, 함수내에서 unpacking된다.

# [**kwargs(언팩킹), **가 붙은게 중요..., 유사 dictionary]
def kwargs_func(**kwargs):                  ## **parameter는 dictionary형태의 key와 value인 것을 넘길 때 사용한다. ## kwargs = dict(name1 = 'Ryu', ...) 인 dictionary를 만드다 생각하면 됨
    for v in kwargs.keys():                 ## 아래 선언한 dictionary의 key값이 들어감 (키의 갯수로 for구문 반복)
        print("{}".format(v), kwargs[v])    ## .format(v)는 keys를 {}에 넣어줌, kwargs[v]에 v는 key를 받으므로 kwargs[v]는 value를 출력한다.
    print('-----')

kwargs_func(name1 = 'Ryu')                  ## 참고로 dictionary변수를 만들때,
kwargs_func(name1 = 'Ryu', name2 = 'Park')  ## a = dict(name1 = 'Ryu', name2 = 'Park')의 형태로 ()를 사용하여 key가 문자열이라도 ''의 사용을 피할 수 있다.
kwargs_func(name1 = 'Ryu', name2 = 'Park', name = 'cho')    ## key가 n개일때는 for문 n번반복

# [전체 혼합]
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Ryu', 'kim', 'Park', age1=20, age2=30, age3=40)
## 10, 20은 순서대로 args_1, args_2에 들어간다.
## *args    : 'Ryu', 'kim', 'Park'를 할당받음        ->  ('Ryu', 'kim', 'Park')
## **kwargs : age1=20, age2=30, age3=40을 할당받음   ->  {'age1': 20, 'age2': 30, 'age3': 40}

print()

# [중첩함수]
# 내부에 있는 함수를 외부에서 호출할 경우 에러가 생긴다.
# 내부에 선언된 함수(자식함수) 외부함수(부모함수)가 선출되지 않는 이상 사용할 수 없다.
def nested_func(num):           ## step2) nested_func(num)이 num=100을 가지고 실행됨
    def func_in_function(num):  ## step3) func_in_function(num)선언, step6) func_in_function(200)이 실행됨
        print(num)              ## step7) 최종적으로, 200이 인쇄
    print("In func")            ## step4) In func 인쇄
    func_in_function(num + 100) ## step5) func_in_function()가 호출됨, 이때 200이 들어감

nested_func(100)                ## step1) nested_func()가 호출됨

print()

# [람다식 예제]
# 장점 : 메모리 절약, 가독성 향상, 코드 간결
# 단점 : 너무 남발시 가독성이 오히려 감소
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 사용방법이 똑같아, 람다식을 쓰느냐 함수를 쓰느냐는 사용자의 취향이다.

## 함수식 선언
##  def mul_func(x, y):
##       return x * y

## 람다식 선언
##  lambda x, y : x * y       ## x, y의 인자를 받고 :뒤에 x * y를 반환

## 일반적 함수 -> 할당
def mul_func(x, y):
    return x * y

print(mul_func(10, 50))
mul_func_var = mul_func
print(mul_func_var(20, 50))

## 람다 함수 -> 할당
lambda_mul_func = lambda x,y : x * y
print(lambda_mul_func(50, 50))

def func_final(x, y, func):
    print('>>>>>', x * y * func(100, 100))

func_final(10, 20, lambda x, y : x * y)
