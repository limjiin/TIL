# Control statement란?
## 프로그램의 흐름을 제어하는 명령어를 말한다.
## 프로그램의 흐름 = 컴퓨터가 어떤 일을 해야하는지에 대한 과정.
## 조건과 반복에 따라서 프로그램의 진행 과정이 바뀌게 된다.
## 프로그램은 조건과 반복의 나열이다.
## 조건(Conditional Statement)로는 if문이 있다.

# if, elif, else
## 반복(Iterative Statement)로는 while, for문이 있다.

# while, for
## 사실상 프로그래밍이란 데이터를 사용자가 원하는대로 제어하여 원하는 결과를 내는 과정을 얘기한다.

# If statement (조건문)
## 프로그램에서 가장 중요한 조건 판단이다.
## 모든 프로그램은 조건을 판단하여 다음 진행 과정을 결정한다.
## 파이썬은 if, elif, else 구문을 이용하여 조건을 사용할 수 있다.

## 같다, 다르다, 크다, 작다, 크거나 같다, 작거나 같다
## ==, !=, >, <, >=, <=

## A and B
## a and b # 둘 다 만족
## A or B
## a or b # 하나 이상 만족
## not A
## not a # a가 아닌 것

# Iterative Statement (반복문)
## 프로그램에서 가장 중요한 반복이다.
## 파이썬에서는 while, for 2가지의 statement를 제공한다.

# While statement
## while문은 조건을 만족할 때 까지 반복한다.
## while (조건):
##   <statement1>
##   <statement2>
##   <statement3>
## 조건이 만족하는 동안(while) statement1, 2, 3을 반복한다.

# for statement
## while문은 조건이 만족하는 동안 반복을 수행했지만, for문은 지정 횟수동안 반복을 수행한다.
## 여기서 지정된 횟수라는 것은 반복 대상의 크기가 된다.
## 보통 iteratable object(반복 가능한 객체)를 대상으로 수행되며, 연속형 데이터 타입 변수들이 여기에 해당된다.
## List, Tuple, string, ...
## for 변수 in 리스트(튜플, 문자열, iterator):
##   <statement1>
##   <statement2>
##   <statement3>
## 리스트(나 반복가능한 변수들)의 모든 원소를 (자동으로 끝까지) 반복한다.

## for문의 단짝 range() 함수
### for문은 특정 횟수동안 반복을 하기 때문에, 횟수를 자동으로 만들어주는 기능이 있으면 좋다.
### 파이썬에서 기본적으로 제공하는 range 함수는 특정 숫자 범위내의 값들을 자동으로 생성해주는 함수이다.
### e.g. range(1, 5)는 1, 2, 3, 4를 차례대로 생성해준다. (5는 범위에서 제외된다. 즉, 마지막 숫자는 제외된다. 1 <= x < 5)








