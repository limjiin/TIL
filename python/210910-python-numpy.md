# Numpy (Numeric python)
> 패키지 이름과 같이 **수리적 파이썬 활용**을 위한 파이썬 패키지
> **선형대수학 구현**과 **과학적 컴퓨팅 연산**을 위한 함수를 제공
> (key) `nparray` 다차원 배열을 사용하여 **벡터의 산술 연산**이 가능
> **브로드캐스팅**을 활용하여 shape(형태 혹은 모양)이 다른 데이터의 연산이 가능
> 기존 언어에서는 제공 X
> 굉장히 파워풀한 기능으로서 빅데이터 연산에 굉장히 효율이 좋음

#### Numpy 사용을 위해 패키지 불러들이기

<pre>
<code>
import numpy as np
</code>
</pre>

> 관례적으로 np라는 약자를 많이 사용하게 됩니다.
> 파이썬을 사용하는 대부분의 유저들이 사용하고 있는 닉네임이니 이건 꼭 지켜서 사
용해주시는 것을 추천드립니다.

#### 데이터분석을 위한 잠깐의 선형대수학

> 데이터의 구분에 따른 표현 방법과 예시

- 스칼라

<pre>
<code>
    1, 3.14, 실수 혹은 정수
</code>
</pre>

- 벡터

<pre>
<code>
    [1, 2, 3, 4], 문자열
</code>
</pre>

- 3 X 4 매트릭스

<pre>
<code>
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 0, 11, 12]]
</code>
</pre>

- 2 X 3 X 4 텐서

<pre>
<code>
   [[[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 0, 11, 12]],
     [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 0, 11, 12]]]
</code>
</pre>

> 데이터 형태에 따른 사칙연산
- 스칼라 +, -, *, / -> 결과도 스칼라
- 벡터 +, -, 내적 -> +, - 결과는 벡터, 내적 결과는 스칼라
- 매트릭스 +, -, *, /
- 텐서 +, -, *, /

> *벡터와 벡터의 내적이 이루어지려면
- 1. 벡터가 마주하는 shape의 갯수(길이)가 같아야 합니다.
- 2. 연산 앞에 위치한 벡터는 전치(transpose) 되어야 합니다.
- (2, 1) <> (1, 2) : 1 끼리 묶임
- (2, 3) <> (3, 4) : 3 끼리 묶임

#### 브로드캐스팅
> 파이썬 넘파이 연산은 브로드캐스팅을 지원합니다.
> 벡터연산 시 shape이 큰 벡터의 길이만큼 shape이 작은 벡터가 연장되어 연산됩니다
.

#### Numpy function(함수) - 유니버셜 함수
> `numpy`는 컴퓨팅연산을 위한 다양한 연산함수를 제공합니다.
> 연산함수 기본구조
> ex) **`np.sum`**(연산대상, axis=연산방향)
> **`dtype()`**

###### 수리연산
- **`prod()`**
- **`dot()`**
- **`sum()`**
- **`cumprod()`**
- **`cumsum()`**
- **`abs()`**
- **`sqaure()`** 제곱
- **`sqrt()`** 루
- **`exp()`** 지수
- **`log()`**

###### 통계연산
- **`mean()`**
- **`std()`**
- **`var()`**
- **`max()`**
- **`min()`**
- **`argmax()`** 최댓값 인덱스
- **`argmin()`** 최솟값 인덱스

###### 로직연산
- **`arange()`**
- **`isnan()`** 값이 있는지 없는지
- **`isinf()`** 무한대
- **`unique()`** 고유값

###### 기하
- **`shape()`**
- **`reshape()`** 모양 변경
- **`ndim()`**
- **`transpose()`** 데이터 위치 변경 전치 행렬

#### numpy 함수 실습
> 함수 예제를 위한 데이터셋

<pre>
<code>
test_list = [1, 2, 3, 4]
test_list2 = [[1, 3], [5, 7]]
test_flist = [1, 3.14, -4.5]
test_list_2nd = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
test_list_3rd = [[[1, 2, 3, 4],
              [5, 6, 7, 8]],

              [[1, 2, 3, 4],
               [5, 6, 7, 8]],

              [[1, 2, 3, 4],
               [5, 6, 7, 8]]]
test_exp = [0, 1, 10]
test_nan = [0, np.nan, np.inf]
</code>
</pre>

- 곱연산

<pre>
<code>
np.prod(test_list)
</code>
</pre>

- 누적곱연산
[O
<pre>
<code>
np.cumprod(test_list)
</code>
</pre>

- 누적합연산

<pre>
<code>
np.cumsum(test_list)
</code>
</pre>

- 절대값
<pre>
<code>
np.abs(test_flist)
</code>
</pre>

- 평균

<pre>
<code>
np.mean(test_list)
</code>
</pre>

- 표준편차
<pre>
<code>
np.std(test_list)
</code>
</pre>

- 분산

<pre>
<code>
np.var(test_list)
</code>
</pre>

- 최댓값 인덱스
> 자주 사용합니다.
> 최대값이 존재하고 있는 인덱스 넘버를 리턴
> 출력값이 인덱스

<pre>
<code>
np.argmax(test_list_2nd)
</code>
</pre>

- 최소값 인덱스

<pre>
<code>
np.argmin(test_list_2nd)
</code>
</pre>

- 범위설정
> (start point, end point - 1, 스텝수)
> range() 함수와 동일하게 작동함

<pre>
<code>
for i in range(0, 100, 10):
     print(i)

np.arange(10, 101, 10)
</code>
</pre>

- 데이터 갯수 사이 범위 설정
> 시작 포인트, 마지막 포인트 - 1, 데이터 갯수

<pre>
<code>
np.linspace(0, 10, 150)
</code>
</pre>

- 결측 확인

<pre>
<code>
np.isnan(test_nan)
</code>
</pre>

- 발산 확인(무한대)

<pre>
<code>
np.isinf(test_nan)
</code>
</pre>

- 고유값 확인

<pre>
<code>
np.unique(test_list_3rd)
</code>
</pre>

- 고유값 갯수 확인

<pre>
<code>
len(np.unique(test_list_3rd))
</code>
</pre>

- 데이터 구조(모양)확인
> 세로, 가로, value 갯수

<pre>
<code>
np.shape(test_list_3rd)
</code>
</pre>

- 데이터 shape 변경
> 어떤 조건에서 reshape 가능한가? 데이터 내부에 존재하는 속성 갯수가 같아야 함.

<pre>
<code>
np.reshape(test_list_3rd, (3, 8))
- 3 * 2 * 4 = 2 * 2 * 6 = 4 * 6 = 3 * 8
</code>
</pre>

- 데이터 차원확인
> 데이터가 존재하는 축방향이 늘어나면 차원 수도 늘어남
> 매트릭스는 2차원 데이터임.
> 데이터 분석에서는 열 기준으로 차원을 이야기함

<pre>
<code>
np.ndim(test_list_3rd)
</code>
</pre>

- 전치 행렬

<pre>
<code>
test_list_2nd
[[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

np.transpose(test_list_2nd)

array([[1, 4, 7],
       [2, 5, 8],
       [3, 6, 9]])

- 2 <> 4, 3 <> 7, 6 <> 8 = 전치 행렬
</code>
</pre>

#### Numpy array (배열, 행렬)
> numpy 연산의 기본이 되는 데이터 구조입니다.
> 리스트보다 간편하게 만들 수 있으며 **연산이 빠른** 장점이 있습니다.
> **브로드캐스팅 연산을 지원**합니다.
> 단, **같은 type**의 데이터만 저장 가능합니다.
> array 또한 numpy의 기본 함수로서 생성 가능합니다.
> array 함수 호출 기본구조
- ex) **`np.array(배열변환 대상 데이터)`**
- ex) **`np.arange(start, end-1, step_forward)`**

- 기존 데이터 구조를 array로 변환

<pre>
<code>
test_array = np.array(test_list)

- '3'  -> str도 들어감

array_list = [1, 2, 4.5]
</code>
</pre>

- np.arange 함수로 생성
> 단 reshape에 들어가는 숫자 2개의 곱은 arange의 수와 일치해야 함

<pre>
<code>
np.arange(35).reshape(5, 7)
</code>
</pre>

- 특수한 형태의 array를 함수로 생성
> 함수 호출의 기본구조
> ex) **`np.ones([자료구조 shape])`**

#### 자료구조 shape은 정수, **[ ]**리스트, **( )** 튜플 로만 입력가능합니다.
- ones()
- zeros()
- empty()
- eye()

- 1로 초기화한 array 생성

<pre>
<code>
np.ones([3,3])
</code>
</pre>

- 0으로 초기화

<pre>
<code>
np.zeros([5, 5])
</code>
</pre>

- 빈 값으로 초기화

<pre>
<code>
np.empty([3, 3])

np.arange(9).reshape(3,3) @ np.eye(3,3)
</code>
</pre>

- 항등행렬 초기화
> 항등행렬의 수학적 의미는 항등행렬 X A = A
> shape이 안맞는 경우 연산이 가능하도록 할 때

<pre>
<code>
np.eye(3, 3)
</code>
</pre>

#### array 속성 및 내장함수
> `np.array` 에는 유용한 수리, 통계 연산을 위한 함수가 갖추어져 있습니다. 다차원
 기하학적 연산을 위한 함수도 함께 살펴보겠습니다.

> array 내장 속성 호출 기본구조
> 자주 사용하는 속성 `shape`, `dtype`, `ndim`
- ex) **`test_array.ndim`**

> array 내장함수 호출 기본구조
> 위에 학습한 np.sum() 과는 달리 array 변수의 인자를 받아 그대로 사용합니다.
- ex) **`test_array.prod()`**

- 데이터 타입확인
> 윈도우는 자동으로 메모리 감축 때문에 64가 아닐 수도 있음

<pre>
<code>
test_array_3rd.dtype

test_array_3rd = np.array(test_array_3rd, dtype = np.int64)
</code>
</pre>

- 데이터구조 확인

<pre>
<code>
np.shape()
test_array_3rd.shape
</code>
</pre>

- 데이터 차원 확인

<pre>
<code>
test_array_3rd.ndim
</code>
</pre>

- 전치행렬(transpose)
> 아래 행렬에 대해서도 데이터의 shape과 차원을 확인해봅니다.

<pre>
<code>
test_array_3rd.T
</code>
</pre>

- 유니버셜 함수를 array에서도 동일하게 사용이 가능하다.
> 내장함수 호출

<pre>
<code>
test_array.sum()
</code>
</pre>

- 누적합

<pre>
<code>
test_array.cumsum()
</code>
</pre>

- 단 array에서 지원하지 않는 squrt는 따로 빼서 사용해야 함

<pre>
<code>
np.sqrt(test_array)
</code>
</pre>

- 평균

<pre>
<code>
test_array.mean()
</code>
</pre>

#### array 연산
> 컴퓨팅 연산을 위한 패키지인 만큼 편리한 배열 연산 기능을 지원합니다.
> 여러 array 연산을 통해 다른 자료구조와의 연산 차이를 알아봅시다.

<pre>
<code>
test_list = [2, 3, 4, 5, 6]
test_list + [7]
test_list * 2 # 벡터 연산은 아님
</code>
</pre>

- 에러 발생

<pre>
<code>
test_list + 7
</code>
</pre>

- array 덧셈, 뺄셈, 곱셈, 나눗셈

<pre>
<code>
test_array * 10
</code>
</pre>

- 비교 연산자 사용도 가능하다.

<pre>
<code>
test_array > 1
</code>
</pre>

- 빠른 연산이 힘들다.

<pre>
<code>
test_list2 = [x * 2 for x in test_list]
test_list2
</code>
</pre>

- 실제 연산속도 차이를 확인하기 위한 큰 데이터 생성

<pre>
<code>
big_list = [x for x in range(400000)]
big_array = np.array(big_list)
len(big_list)

%%time
big_list2 = [x + 1 for x in big_list]
</code>
</pre>

#### 행렬내적

<pre>
<code>
first_array = np.arange(15).reshape(5, 3)
second_array = np.arange(15).reshape(3, 5)
</code>
</pre>

- 행렬내적 연산

<pre>
<code>
first_array.shape + second_array.shape
</code>
</pre>

#### 벡터 가중합
> 벡터의 내적은 가중합을 계산할 때 쓰일 수 있다.
> **가중합(weighted sum)**이란 복수의 데이터를 단순히 합하는 것이 아니라 각각의 수에 어떤 가중치 값을 곱한 후 이 곱셈 결과들을 다시 합한 것을 말한다.
> 만약 데이터 벡터가 $x=[x_1, \cdots, x_N]^T$이고 가중치 벡터가 $w=[w_1, \cdots, w_N]^T$이면 데이터 벡터의 가중합은 다음과 같다.

<pre>
<code>
$$
\begin{align}
w_1 x_1 + \cdots + w_N x_N = \sum_{i=1}^N w_i x_i
\end{align}
$$
</code>
</pre>

> 이 값을 벡터 $x$와 $w$의 곱으로 나타내면 $w^Tx$ 또는 $x^Tw$ 라는 간단한 수식으
로 표시할 수 있다.
> 쇼핑을 할 때 각 물건의 가격은 데이터 벡터, 각 물건의 수량은 가중치로 생각하여 내적을 구하면 총금액을 계산할 수 있다.

##### 벡터의 가중합 연습문제
> 삼성전자, 셀트리온, 카카오로 포트폴리오를 구성하려한다.
> 각 종목의 가격은 80,000원, 270,000원, 160,000원이다.
> 삼성전자 100주, 셀트리온 30주, 카카오 50주로 구성하기 위한 매수금액을 구하시오

<pre>
<code>
stocks = np.array([100, 30, 50])
price = np.array([80000, 270000, 160000])
total = stocks @ price
total
</code>
</pre>

- transpose() : 데이터 위치 변경, 전치 행렬

<pre>
<code>
price.T
</code>
</pre>

#### array 인덱싱, 슬라이싱(매우중요)
> 기본적으로 자료구조란 데이터의 묶음, 그 묶음을 관리 할 수 있는 바구니를 이야기
 합니다.
> 데이터 분석을 위해 자료구조를 사용하지만 자료구조안 내용에 접근을 해야 할 경우
도 있습니다.
> **인덱싱**이란?
> 데이터 바구니 안에 든 내용 하나에 접근하는 명령, 인덱스는 내용의 순번
> **슬라이싱**이란?
> 데이터 바구니 안에 든 내용 여러가지에 접근 하는 명령
> 기본적으로 인덱싱과 슬라이싱의 색인은 리스트와 동일합니다.

- 0부터 3번 인덱스까지

<pre>
<code>
a[:4]
</code>
</pre>

- 4번 인덱스부터 마지막 인덱스까지

<pre>
<code>
a[4:]
</code>
</pre>

- 마지막 인덱스부터 뒤에서 3번째 인덱스까지

<pre>
<code>
a[-1:-4:-1]
</code>
</pre>

- 0부터 3씩 증가하는 인덱스

<pre>
<code>
a[::3]
</code>
</pre>

- 매트릭스 인덱스 구하기
> 행 기준, 열 기준

<pre>
<code>
index_test2[2:,1:4]
</code>
</pre>

- 벡터 인덱스 구하기

<pre>
<code>
index_test3[0, 3:,1:3]

index_test3[:, :, 1]
</code>
</pre>

#### 팬시 인덱싱
> numpy에서 벡터 연산을 통해 bool 형태(true, false)의 벡터를 기준으로 데이터를 >선별하는 방법이다.

<pre>
<code>
pet = np.array(['개', '고양이', '고양이', '햄스터', '개', '햄스터'])
num = np.array([1, 2, 3, 4, 5, 6])
indexing_test = np.random.randn(6,5)
</code>
</pre>

> random.randn : 난수로서 행렬을 만들어주는 함수

- 인덱싱

<pre>
<code>
indexing_test
indexing_test[pet == '개']
</code>
</pre>

- true and false

<pre>
<code>
num > 5
pet == '개'

(pet == '개') | (pet == '햄스터')
산
(pet == '개') != (pet == '햄스터')
</code>
</pre>

- '개'의 갯수 합

<pre>
<code>
(pet == '개').sum()
</code>
</pre>

- 하나라도 있다면 출력

<pre>
<code>
(pet == '개').any()
</code>
</pre>

- 전체 데이터가 '개'인지

<pre>
<code>
(pet == '개').all()
</code>
</pre>

