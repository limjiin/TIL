# 연속형 데이터 (Sequential Data Types)
## 연속형 데이터 타입에는 리스트(List), 튜플(Tuple), 문자열(String)이 있다. (문자열을 문자들의 나열로 인식하기 때문에, 연속형 데이터이다.)
## 연속형 데이터의 크기 제한은 없다. 하지만, 사용하는 컴퓨터의 가용 메모리 용량을 인지하며 사용해야 한다.
## 각 연속형 데이터 타입마다 특징이 다르다. 그 특징을 파악하여 용도에 맞는 데이터 타입을 사용하는 것이 중요하다.
## (OPTIONAL) 사전(dictionary) 타입은 associative array라고 불리며, 흔히 알고있는 Hash table 구조이다.

# 리스트(List)
## 가장 많이 사용되는 연속형 데이터 타입이자, 굉장히 유연한 구조를 가지고 있어 대부분의 데이터를 편하게 다룰 수 있다.
## 파이썬에서 [ ]를 이용하여 표현한다. e.g. [1, 2, 3]
## 리스트의 원소는 쉼표로 구분되며, 리스트의 원소는 아무 데이터 타입이나 가능하다. 리스트조차 가능하다.
## 리스트를 이용하면 파이썬에서 다루는 대부분의 데이터는 아무 무리없이 다룰 수 있다. 하지만 수정이 자유롭기 때문에 수정을 하면 안되는 경우에는 사용하면 안된다.

## Indexing
### 연속형 데이터들은 하나의 변수에 여러가지 데이터를 가지기 때문에 여러 데이터를 접근하는 방법이 필요하다.
### 이를 위해 indexing이라는 기법이 있다. 말그대로 index를 통해 접근(access)하는 방법이다.
### 리스트의 index는 맨 앞부터 0으로 시작하며, 1씩 증가하는 정수 index를 사용한다.
### e.g. [1, 2, 3]이면 첫번째 원소는 index가 0이고, 두번째 원소는 index가 1이다.
### 파이썬에서는 음수 index도 제공하는데, 이는 뒤쪽부터 접근할 수 있는 방법이다.
### e.g. [1, 2, 3]이면 뒤에서 첫번째(맨 마지막)원소는 index가 -1이고, 뒤에서 두번째 원소는 index가 -2이다.
### index를 통해 접근하는 방법은 해당 변수이름에 []를 사용하며, []안에 index를 넣어서 접근할 수 있다.
### e.g L = [1, 2, 3]이면 L[0]은 1이고, L[2]는 L[-1]이며 3이다.

## Slicing
### 슬라이싱은 리스트에서 뿐만 아니라, 리스트와 비슷한 구조인 numpy array와 pandas series, dataframe에서도 많이 이용되니 꼭 알아두어야 한다.
### 슬라이싱은 리스트의 일부분만 잘라낸다는 의미이다. (말그대로 슬라이싱)
### 리스트의 일부만 사용하고 싶을 때 쓰는 기법이며, indexing을 범위로 하는 느낌이다.
### 리스트의 index와 :를 사용하여 슬라이싱을 할 수 있다.
### e.g. L = [1, 2, 3, 4] L[0:2]는 [1, 2]이다.

## list 연산
### 더하기 : L1 + L2
### 곱하기 : L1 * 3
### 수정하기 : L[2] = 1
###            L

## list 함수
### 원소 추가하기: append()
### 원소 정렬하기: sort() cf. sort(reverse=True)
### 뒤집기 : reverse()
### 마지막 행 원소 제거하기 : pop()

# 튜플(Tuple)
## tuple은 list과 거의 같다.
## indexing, slicing 모두 동일하게 사용 가능하다. 원소들도 자유롭게 사용 가능하다.
## 거의 같은데, 다른 점이 딱 2가지 있다.
## 1) 리스트는 []를 사용하고, 튜플은 ()을 사용한다.
## 2) 리스트는 생성 후에 변경이 가능하고(mutable) 튜플은 생성 후에 변경이 불가능하다.(immutable)
## Mutable : 생성된 이후에 변경(assignment)이 자유롭게 가능한 data type. e.g. List, dict, set
## immutable : 생성된 이후에 변경이 불가능한 data type e.g. int, float, string, tuple, frozenset
## 성능적인 이슈 -> 변경되지는 않는 그 자체로 장점이 생김.
## 프로그래밍적인 이슈 -> 데이터 수정 자체를 하지 않는 경우 실수를 방지할 수 있다.

# 집합(Set)
## 집합 자료형은 정말 말그대로 수학에서 배우는 집합 그 자체이다.
## 수학에서는 집합을 {}로 표시했지만, 파이썬에서는 안타까운 이유로 {}를 사용하긴 하는데 그냥 사용할 수는 없다. 왜냐면 사전(Dictionary) 자료형도 {}를 사용하기 때문이다. 이에 대해서는 뒤에 자세히 배운다.
## 공집합을 생성할 때는 반드시 set()으로 생성해야 한다. {}로 생성하면 빈 사전이 생성된다.
## e.g. {1, 2, 3} : 집합, {'a':1, 'b':2} : 사전
## 집합의 연산자인 교집합, 합집합, 차집합을 모두 지원한다.
## 집합의 특징이 2가지 있는데, 이 특징이 리스트와의 차이점이라 사용한다. 첫번째 특징이 집합 자료형을 사용하는 주된 이유이다.
## 1) 집합은 원소의 중복을 허용하지 않는다. 즉, 원소의 종류를 나타내기 좋다.
## 2) 집합은 원소의 순서가 존재하지 않는다. 즉, 원소의 index가 없다.

## 집합의 연산
### 교집합: s1 & s2
### 합집합: s1 | s2
### 차집합: s1 - s2

## 집합 함수
### add()
### update()
### remove()

# 사전(Dictionary)
## 파이썬에서 리스트와 함께 굉장히 많이 사용되는 구조. 특히 이번 교육과정 중에 많이 사용되니 꼭 마스터하는 것을 추천한다.
## 파이썬에서 제공하는 사전 자료형은 key - value 방법을 통해 저장한다.
## Hash Table이라고 불리며 데이터 관리에서 굉장히 중요한 개념이다.
## 파이썬에서 사전 자료형은 {}을 이용하여 표현하는데, 집합과의 차이점을 두기 위해 원소에 반드시 :가 들어가야 한다.
## 사전을 표현할 때는 {key : value, key2 : value2, ... } 형태로 표현한다.
## e.g. {'a' : 1', "b" : 3}
## 사전에서 key가 될 수 있는 data type은 immutable이어야 한다.

## 사전 함수
### keys()
### values()
### items()
### get()