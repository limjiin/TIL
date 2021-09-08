# Function이란?
## input -- function(parameter) -- output
## 수학적인 의미의 함수와 개념은 비슷하지만 역할이 다르다.
## input이 들어와서 output이 정해진 규칙에 따라 나온다는 개념은 같지만, 프로그램에서의 하나의 함수는 하나의 기능을 나타낸다.
## 정확하게 함수는 특정 기능을 구현한 코드 묶음이다.
## def 함수이름(param1, param2, ... ):
##   <statement1>
##   <statement2>
## return
## 함수를 쓰는 이유는 재사용성 때문이다.

### def add(a, b): # 입력받은 a, b를 더한 값을 돌려주는 함수.
###    c = a + b
###    return c # 도구를 만들었음
### add(10,11)

### 가장 흔하게 사용되는 경우 -> 함수 parameter와 return이 모두 존재하는 경우.
### def add(a,b):
###     return a + b
### def get_loss(model, metric):
###    return model.predict(result, metric=[metric])

### 함수 parameter는 없고 return이 존재하는 경우.
### def get_data():
###     data = pd.read_csv("test.csv")
###     return data
### 해야 할 일이 지정되어 있음.

### 함수 parameter는 있는데 return이 없는 경우.
### def print_name(name):
###     print(name)
### def save_data(path, data):
###     data.to_csv(path)
### 출력이나 저장하는 코드로 사용함

### 함수 parameter도 없고 return도 없는 경우.
### def say_hi():
###     print("Hi")
### 간단한 데이터
### def save_txt():
###     with open("test.txt", 'w') as f:
###         f.write(txt)

### parameter가 너무 많아서, 다 외울수도 없다. 이럴 땐 default parameter를 지정해놓고, 필요한 parameter만 입력받는다.
### def defalut_add(a,b=10):
###     return a + b

### 함수에서 사용되는 변수들에게는 효력 범위와 수명이 있습니다.
### 효력범위: range, 수명: lifetime
### def change_name(name): # local variavle, 지역 변수
###    name = "lee" # local
###    print("in function:", name)
### name = "kim" # global
### change_name(name)
### print(name)

# lee, kim

### def change_name(name):
###    name = "lee" # local
### return name
### name = "kim" # global
### name = change_name(name)
### print(name)

# kim


## Lambda 함수를 사용해보자!
## Lambda Expression
## 굉장히 간단한 함수가 있는 경우, 한 줄짜리 함수로 간편하게 사용할 수 있다.
## in line function(줄 안에 있는 기능), def 라고 하는 명령어 없이 간단하게 정의해서 사용할 수 있다.
## 이런 함수를 Lambda 함수라고 하며, lambda 함수와 반복문을 통해 함수의 정의없이 다양한 프로그래밍이 가능하다.

### def add(a, b):
### return a+b

### lambda 함수로 바꾸면?
### f = lambda a, b: a + b # a, b는 input parameter들, a + b는 return 되는 output parameter
### print(add(3,5))
### print(f(3,5))

### strings.sort() # alphabetical order 즉 사전순 정렬

### strings.sort(key = lambda s: len(s)) # 길이에 따라 정렬
### strings

## 수학 계산을 해봅시다.
### import math  

## 절대값, 올림, 내림
### print(abs(-3))
### print(math.ceil(3.5))
### print(math.floor(3.8))

## sin, cos
### a = 3.5
### print(math.sin(a))
### print(math.cos(a))

## 복권 숫자를 만들어봅시다.
### import random
### random.sample(range(1,46),7)
### x범위에서 y개를 뽑아줘.

## 다양한 사전들을 써봅시다.
### from collections import defaultdict
### from collections import OrderedDict

### D = defaultdict(int)
### D2 = OrderedDict()
### D2['a'] = 26
### D2['b'] = 1
### D2['c'] = 3
### D2['d'] = 5
### D2['e'] = 14
### D2['f'] = 2
## D2
