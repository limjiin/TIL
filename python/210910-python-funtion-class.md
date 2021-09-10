## 함수
> 수학적 정의의 **함수**란?  
$y$ = $f(x)$

> 프로그래밍에서의 함수란?  
자주 사용해야 하는 코드를 **재사용하기 위한 코드의 묶음**

> 데이터과학에서의 함수란?  
입력값을 받아 사용자가 원하는 처리를 한 후 결과값을 되돌려 받는 코드의 묶음


### 함수의 구조
>**`def` `함수이름` `(파라메터 혹은 매개변수)` `:`** # 파라메터는 없어도 가능함. 함수 정의 후 `:`으로 마무리 한다.
>>**`실행코드`**
**`실행코드`**
**`실행코드`**
**`return` `반환값`** # 함수에서 실행코드를 거친 결과 값 혹은 변수(반환값)을 리턴

>파라메터 혹은 매개변수 : 함수의 입력값, 혹은 함수의 작동에 영향을 줄 수 있는 값(변수)
파라메터는 없어도 되지만 세미콜론은 반드시 찍어준다.


# 함수 정의하기
# 함수명 person을 정의한다(디파인한다)

# 파라미터는 없다.
def person():
    for i in range(10):
        print('제 이름은 Eddy 입니다.')
# 함수 호출 시 실행 될 구문

# 파라메터가 있는 함수 정의
# 함수명 person_name을 정의하면서 동시에 파라메터인 name에 'Eddy'라는 문자열을 전달한다.
# 디폴트 파라메터 설정도 가능하다.
def person_name(name, age):
    print(f'제 이름은 {name}이고, 나이는 {age}입니다.')
# 함수 호출 시 실행 될 구문


# 함수 밖 변수 '전역변수, 글로벌변수'라고 하며 어디든 사용가능
a = 10
b = 20
def print_num(x):
    global a # 밖에 있는 변수에 값 업데이트나 변수 값을 변경 가능하도록 해주는 키워드
    
    a = a + x # 함수 안에서 사용만을 목적으로 써야하는 값이면 일반적으로 파라미터로 전달합니다.
print_num(b)
# 지역 변수를 글로벌 변수로 사용하고 싶을 시, global로 명시하고 return을 입력해줘야 한다. 

# 그렇다면 함수 내부에서 정의 된 변수는 밖에서 호출이 안됨.
함수 내부에서 정의 된 age 변수는 함수 내부에서만 정의되는 변수로서 함수 밖에서는 호출할 수 없다.
그렇기에 다른 함수에서 같은 이름의 변수를 사용해도 관계없음
함수 연산 결과로서 결과값을 빼기 위해서는 반드시 return구문으로 반환값을 사용해줘야 함
# 함수 내부에서 정의 된 변수는 지역변수 혹은 '로컬변수'라고 합니다.
# 함수 내부에서만 사용이 가능하고 사용후에는 메모리에서 삭제 됩니다.

# 함수 내부에서 정의 된 변수를 사용하기 위해서는 값을 반환(return) 시켜야 한다.
# x와 y를 파라메터로 전달받는 cal_return 함수 정의
# 리턴 값이 여러 개일 수 있음

def cal_val(x, y, z):
    return((x + y) ** z) + z
cal_val(1, 2, 4)

# 사용자로부터 입력받는 5개의 숫자를 리스트에 저장하고 입력이 완료되면 합을 출력하는 함수
def test_sum(a):
    test_list = []
    for i in range(a):
        test_input = int(input('숫자를 입력하세요. ; '))
        test_list.append(test_input)
    print(sum(test_list))
test_sum(10)

# 지금까지 우리가 알게 모르게 사용해왔던 함수들
print()
int()
str()
float()
input()
list()
dict()
range()
append() 등등등

python 예약어로 지정 된 함수를 쪼개봅시다
sum() 함수는 python 언어에 내장되어 있는 함수입니다.
파라메터로 iterable 변수 즉, 반복문으로 내부 인자의 루프를 돌 수 있는 변수를 받습니다.
그리고 그 인자의 합을 출력하는 함수입니다.

max() 함수도 python 내장 함수로서 sum()과 같은 형식의 입력값을 받아 최대값을 반환하는 함수입니다.
함수를 쪼개봅시다

# sum_sum을 함수 이름으로 갖는 python sum() 함수를 재현해보기
# 단 sum()은 쓰지 않기. 전달 받는 데이터가 list 라고 가정한다.
def sum_sum(x):
    total = 0
    for x in test_list:
        total = total + x
    return total

def sum_sum(x):
    total = 0
    for item in x:
        total += item
    return total

# max_max를 함수 이름으로 갖는 python max() 함수를 재현해보기
def max_max(x):
    total = 0
    for item in x:
        if item > (item - 1):
            total = item
    return total

def max_max(x):
    max_val = -9999999
    for item in x:
        if item > max_val:
            max_val = item
    return max_val

# 클래스
>위에서 만든 계산기 함수를 살펴봅시다.  
구조가 같은 함수가 여러개 반환값이 같은 연산만 다른 함수가 있다.  
조금 간편하게 함수를 만들 수 없을까?  

>**클래스**란?  
같은 목적 혹은 대상을 위해 만들어진 **함수들의 묶음**

# 클래스의 구조
> **`class`** **`[클래스명]`** **`:`** # 클래스의 선언

>> **`def`** **`__init__`** **`(self, [파라메터])`** **`:`**
>> 클래스를 만들면서 입력받는 파라메터를 클래스 내에서 사용가능 하도록 초기화
>>> **`self.[변수명]`** = **`[파라메터]`**
>>> 클래스를 만들면서 입력받는 파라메터를 클래스 내에서 사용가능 하도록 초기화
>>> `self.x` = `x`

>>**`def`** **`[함수명]`** **`([self, 파라메터])`** **`:`**
>>>**`[실행코드]`**

> 클래스의 선언은 함수와 달리 소괄호없이 선언한다.
클래스명은 단어의 첫 알파벳을 대문자로 ex) MyClass, SumTotal
클래스 선언이후 처음 작성하는 **`__init__`** 함수는
클래스가 정의되면서 입력되는 파라메터를 저장하고 재사용하기 위한 초기화함수
클래스 내 함수의 파라메터앞에는 항상 **`self`**를 추가해주어야 하며,
**`__init__`** 함수에서 설정한 변수 사용시에도 **`self`** 를 추가해준다.
**`self.`** 변수는 클래스 내부에서 사용되며 클래스 내부에 있는 모든 함수에 사용이 가능하다.

# 클래스의 형태를 눈으로 익혀봅시다.
class Calculator: # 클래스 선언

    def __init__(self, x, y): # 초기화함수
        self.x = x # 클래스 내 변수 초기화
        self.y = y # 재귀 목적, 자기 자신을

    def my_sum(self): # 함수 정의
        z = self.x + self.y
        return z

    def my_minus(self):
        z = self.x - self.y
        return z

    def my_multiply(self):
        z = self.x * self.y
        return z

    def my_division(self):
        z = self.x / self.y
        return z

# 클래스의 호출
a = Calculator(3, 5)
# 클래스 내 함수의 호출
a.my_division()

그럼 클래스와 함수는 항상 만들어 써야할까?
절대 그렇지 않습니다. 오히려 이미 만들어져있는 함수를 가져다 쓰는것을 권장합니다.
프로그래밍 혹은 데이터분석에 필요한 수많은 함수들이 이미 만들어져 있습니다.
함수를 학습하는 이유는 이러한 함수들을 호출하여 쓸 수 있게 하기 위함입니다.

import [패키지명]
import [패키지명] as [닉네임]
from [패키지명] import [함수명]

!dir
# 파일이 속한 폴더 내 모든 파일

pwd
# 현재 폴더 위치

# 이런것도 할 수 있어요~
# 텍스트를 음성으로 변환시켜주는 패키지(모듈) 입니다.
# 사용하기 전 패키지를 다운받는 과정이 필요합니다.
# pip install pyttsx3
import pyttsx3
engine = pyttsx3.init()
engine.say("수강생여러분.")
engine.say("파이썬 공부하느라 고생하십니다.")
engine.say("파이썬으로 이런것도 가능해요")
engine.say("하지만 이해못해도 괜챦아요.")
engine.say("왜냐하면 우리는 가져다 쓸꺼니까요. 찡긋")
engine.runAndWait()

# random 이라는 이름을 가진 모듈을 불러오기
import random

# random 패키지를 사용해보자
>**`random`** 은 파이썬 내장 패키지(모듈)입니다.  
랜덤한 값을 생성하거나 뽑아오는데 사용합니다.

>**`random`** 모듈 불러오기
**`import`** **`random`**

>`random` 모듈의 자주 사용하는 함수  
`random` `.random()` : 0 ~ 1 사이의 실수를 하나 반환  
`random` `.randint(a, b)` : a ~ b 사이의 정수를 하나 반환  
`random` `.choice`(list 혹은 데이터집합) : list의 무작위 샘플하나를 반환  
`random` `.sample`(list 혹은 데이터집합, N(샘플링 할 데이터의 갯수)) : list의 무작위 샘플  N개를 반환  
`random` `.suffle`(list 혹은 데이터집합) : list 순서 섞기  

# 0 ~ 1 사이의 실수를 하나 반환
random.random()

# list의 무작위 샘플  N개를 반환
random.sample(range(1, 45), 4)

# a ~ b 사이의 정수를 하나 반환
random.randint(1, 45)

# list의 무작위 샘플하나를 반환
random.choice(test_list)

# list 순서 섞기
random.shuffle(test_list)
test_list

## 로또 만들기

# 심플하게 6개 숫자를 만들어봅시다.
random.sample(range(1, 10),6)

lotto = []
for i in range(6):
    lotto.append(random.randint(1, 45))
lotto

# 중복숫자 제거
# 정답은 없습니다. 각자가 구현할 수 있는 방법을 강구해서 중복숫자를 제거하고 번호 6개를 생성해 봅시다.
lotto = []
for num in range(6):
    num = random.randint(1, 45)
    if num in lotto:
        pass
    else:
        lotto.append(num)
lotto

# 누가 로또를 하나만 사나요? 최소 5000원짜리 한세트를 사지요
# 5세트 만들어봅시다
total_lotto = []
for i in range(5):
    lotto = []
    for num in range(6):
        num = random.randint(1, 45)
        if num in lotto:
            pass
        else:
            lotto.append(num)
    total_lotto.append(lotto)
total_lotto

연습문제 스무고개 게임 업그레이드
컴퓨터와 스무고개 게임을 하는 프로그램을 만들어보겠습니다.
random 모듈로 컴퓨터가 1 ~ 100 중 숫자를 하나 선택하게 합니다.
게이머에게 입력받은 숫자를 판별하여 업, 다운, 정답을 출력하는 프로그램입니다.
게임 횟수는 10회이며, 10회 동안 정답을 못 맞출 경우 실패 문구를 출력하도록 프로그램을 짜 보겠습니다.
선택) 사용자에게 최소숫자, 최대숫자를 입력받아 random으로 생성

def step_game(x, y):
    computer = random.randint(x, y)
    count = 10
    while count > 0:
        player = int(input('숫자를 입력하세요:'))
        if computer > player:
            print(f'업, {count}번 남았습니다.')
            count = count -1
        elif computer < player:
            print(f'다운, {count}번 남았습니다.')
            count = count -1
        elif computer == player:
            print('정답')
            break
        if count == 0:
            print('실패입니다.')
    print('게임이 종료되었습니다.')


# numpy 패키지을 불러오고 np라는 닉네임으로 사용한다
import numpy as np

# pandas 패키지를 불러오고 pd라는 닉네임으로 사용한다
import pandas as pd



