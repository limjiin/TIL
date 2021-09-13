## Pandas
> 데이터 과학자를 위해 **테이블형태**로 데이터를 다룰 수 있게 해주는 패키지(python용 엑셀)
> 기존 데이터처리 라이브러리인 numpy 대신 주로 사용
> 일반인이 데이터분석을 접하기 쉽게 만들어준 결정적인 라이브러리
> pandas만으로도 충분히 데이터 분석이 가능할 정도로 고수준의 함수들을 내장
> 앞으로 진행하는 데이터분석 과정에서 주로 사용하게 될 데이터구조

<pre>
<code>
# pandas 설치
!pip install pandas

# numpy import
import numpy as np

# pandas import
import pandas as pd
# pd라는 닉네임은 많은 파이썬 유저들이 사용하고 있는 닉네임, 분석을 위한 필수는 아니지만 되도록이면 위와 같이 사용을 해줍시다.

pd.options.display.max_columns = 200
# 불러들이는 데이터에 맞춰 모든 컬럼을 확인 가능하도록 옵션값을 주었습니다.
pd.options.display.max_info_columns = 200
# 그냥 실행 시키시고 지금 이해 못하셔도 좋습니다.
</code>
</pre>

## DataFrame
> 엑셀에 익숙한 사용자를 위해 제작 된 **테이블형태의 데이터 구조**
> 다양한 형태의 데이터를 받아 사용할 수 있으며 다양한 **통계, 시각화 함수를 제공
**한다.

#### 데이터 불러오기
pandas는 다양한 데이터 파일 형태를 지원하며 주로 csv, xlsx, sql, json을 사용합니
다.

- **`read_csv()`**
- **`read_excel()`**
- **`read_sql()`**
- **`read_json()`**
- **`json_normalize()`**

<pre>
<code>
# DataFrame 의 약자로서 형식적으로 df 변수명을 사용한다.
# pandas패키지의 read_csv() 함수를 사용하여 loan.csv 파일을 불러들여 데이터프레>임을 만들고 df 이름의 변수로 저장
df = pd.read_csv('./data/loan1.csv')
df
</code>
</pre>

##### 참고! 쿼리를 사용하여 데이터베이스로부터 데이터프레임을 만드는 것도 가능합
니다.
> 데이터베이스로 부터 자료 읽기

<pre>
<code>
# 필요한 모듈 추가 설치 - 각 데이터베이스 별로 다릅니다.
!pip install pymysql

# sql 모듈 로드하기
import pymysql
# mysql, mariadb, sqlite, postgresql, ms-sql, oracle, mongodb

# 접속하기
# 접속방법 또한 DB 종류에 따라 다릅니다.
con = pymysql.connect(host='db서버주소', port=3306, user='id', passwd='pwd', db='dbname')

# query 만들기
query = 'select * from samples'

# 자료 불러오기
data = pd.read_sql(query, con=con)
</code>
</pre>

## 데이터 저장하기
> 불러들인 혹은 작업을 마친 데이터프레임을 다양한 파일형태로 저장이 가능합니다.

- **`to_csv()`**
- **`to_excel()`**
- **`to_sql()`**

<pre>
<code>
# index=False 파라메터는 기존 데이터프레임의 인덱스를 무시하고 저장
df.to_csv('./data/save_test.csv', index=False)

df.to_csv('./data/save_test.csv.gz', index=False)
# 보안 프로그램을 피할 수 있음
# gz = 압축파일

# 참고
df1 = pd.read_excel('./data/loan1.xlsb',
                    sheet_name='',
                    engine='pyxlsb'
                    encoding='utf-8') # 윈도우는 cp949
</code>
</pre>

- 참고 : [pandas document](https://pandas.pydata.org/docs/)

## 데이터 살펴보기
> 데이터를 불러들인 후 가장 처음 하는 작업
> 데이터의 구조, 형태 파악하기

<pre>
<code>
# 데이터의 첫 5개 샘플 확인하기
df.head()
# 10개를 확인하려면?
df.head(10)

# 데이터의 마지막 5개 샘플 확인하기
# 데이터가 잘 가져왔는지 확인 할 때 보통 씁니다.
df.tail()

# 데이터의 갯수를 살펴봅니다
len(df)
# 데이터의 전반적인 정보를 확인합니다.
df.info()
# dtype 정보에서는 각 컬럼별 데이터 타입을 확인 할 수 있습니다.
# object == str 이라고 생각하셔도 무방합니다.
# verbose, null_counts

# 데이터의 기초통계량을 확인합니다.
df.describe()

# numpy 함수로 데이터 shape 확인
np.shape(df)

# 인덱스
df.index

# 컬럼
df.columns
</code>
</pre>

## 데이터 접근(인덱싱, 슬라이싱, 샘플링)
> 첫 샘플 혹은 레코드(대출건)에 대한 데이터를 살펴보겠습니다.
> 인덱스넘버로 데이터에 접근하는 .iloc[색인]
> 각 컬럼이나, 행단위 접근했을 때 출력되는 백터 데이터를 Serise (시리즈) 라고 하
는 자료 구조
> index, values 로 각각의 속성에 접근 가능

<pre>
<code>
df.iloc[0]
# df.iloc[0].index
# df.iloc[0].values

# 10번 인덱스 부터 20번 인덱스 샘플 접근
# start, end+1,
df.iloc[10:20:2]

# 첫번째 0, 10, 20 인덱스 샘플 접근
df.iloc[[0, 10, 20]]
= df.take([0, 10, 20])
</code>
</pre>

#### 컬럼 단위 샘플 접근
> 열벡터 -> 시리즈
> 인덱싱이나 슬라이싱으로 데이터에 접근을 할 때 큰 단위를 선택하고 그 결과에서 >인덱싱 혹은 슬라이싱을 하면
> 조금 더 편하게, 쉽게 데이터 접근이 가능하다.

<pre>
<code>
df['emp_title'].values
# df[텍스트형태의 컬럼명]

# dict
test_dict['key']
values

# 여러 컬럼 동시 접근
df[['emp_title', 'int_rate']]
</code>
</pre>

#### df.loc[인덱스, 컬럼명]
> row와 columns을 동시에 슬라이싱 하는 속성

<pre>
<code>
df.loc[100:200, df.columns[0:10]]

# df의 컬럼명을 순환하면서 컬럼 단위로 접근하고 각 컬럼의 고유값을 출력해주는 코
드가 된다.
for col_nm in df.columns:
    print(col_nm, df[col_nm].unique())

# 고유값 갯수 출력 고유값 갯수 출력
for col_nm in df.columns:
    print(col_nm, df[col_nm].nunique())
</code>
</pre>

## 팬시인덱싱
> **`bool`** 형태의 array를 조건을 전달하여 다차원 배열을 인덱싱하는 방법.
> 조건식을 사용하여 분석에 필요한 데이터샘플을 추출하기 용이합니다.

<pre>
<code>
# 신용등급이 A인 샘플의 emp_title 확인
df[df['grade'] == 'A']['emp_title'].unique()

# 대출금액평균
df['loan_amnt'].mean(), 0

# 조건식 샘플링 emp_title 이 ceo인 샘플들
df[df['emp_title'] == 'ceo']

# 신용등급 A와 B인 샘플접근
df[(df['grade'] == 'A') | (df['grade'] == 'B')]
# 조건식을 여러개 써야 한다면 조건마다 ()로 감싸주시는 것이 좋습니다.

# df loan_amnt 컬럼값이 10000이상인 채권샘플의 grade
df[df['loan_amnt'] >= 10000]['grade']
# value_counts() 고유값의 갯수
# unique
# nunique

# df grade C 와 D 인 채권샘플 emp_title
# 옵션 annual_inc 최대값인 인덱스 빼오기
# idxmax() = argmax
df3 = df[(df['grade'] == 'C') | (df['grade'] == 'D')][['emp_title', 'annual_inc']]
df3['annual_inc'].idxmax()

= df.iloc[df[(df['grade'] == 'C') | (df['grade'] == 'D')]['annual_inc'].idxmax()]['emp_title']

# 컬럼 내 문자열 내에 우리가 찾고 싶은 문자열이 포함되어 있는지를 기준으로 샘플>링
df['emp_title'].str.contains('Manager')
</code>
</pre>

## 데이터프레임 병합
> 실제 분석업무를 진행하다보면 데이터가 여기저기 분산되어 있을 경우가 더 많습니>다.
> 조각난 데이터를 분석에 필요한 데이터셋으로 만들기 위해 데이터프레임 병합을 많>이 사용합니다.
> 한개 이상의 데이터프레임을 병합 할 때 주로 사용하는 함수 2가지를 알아보겠습니>다.

#### 데이터 병합에 사용가능한 key(병합할 기준이 되는 행 or 열)값이 있는경우
> **`pd.merge`**(베이스데이터프레임, 병합할데이터프레임)
> 사용 가능 한 파라메터
- `how` : 'left', 'right', 'inner', 'outer'
- `left_on` : key값이 다를 경우 베이스데이터프레임의 key 설정
- `right_on` : key값이 다를 경우 병합데이터프레임의 key 설정

#### 단순 데이터 연결
> **`pd.concat`**([베이스데이터프레임, 병합할데이터프레임], axis=0 or 1)
> 사용 가능 한 파라메터
- `axis` : 축 방향 설정

- merge 예시

<pre>
<code>
pd.merge(merge_df1, merge_df2, how='right') # left, inner, outer

pd.merge(merge_df3, merge_df4, how='outer', left_on='이름', right_on='name')
</code>
</pre>

- concat 예시
> 현재 df에 저장되어있는 데이터에 추가로 2만개의 데이터를 이어붙여보겠습니다.
> df1이라는 변수에 이어붙일 데이터를 불러들여 병합을 진행해보겠습니다.
> 즉, 갖다 붙인다고 생각하면 됨

<pre>
<code>
# df 와 df1 shape 확인
df.shape, df1.shape
df.columns == df1.columns
# 데이터프레임 행단위 병합
concat_df = pd.concat([df, df1])
# 깔끔한 처리를 위해서 : ignor_index=True 또는 axis = 1

# 데이터인덱스 확인
concat_df.index
# 인덱스가 틀어짐

# 병합 데이터프레임 shape 확인
concat_df.shape
</code>
</pre>

- index 편집

<pre>
<code>
concat_df.iloc[0]

# 인덱스리셋
concat_df.reset_index(drop=True)
# drop - 현재 인덱스의 원본값을 버림 : 기존 인덱스값을 날리면서 인덱스 초기화
# inplace - 원본값 변경

# 기존 컬럼값을 취해 index로 사용
concat_df.set_index('id')
</code>
</pre>

- columns 편집

<pre>
<code>
# df 컬럼명 접근
df.columns[:25]

# columns 속성도 인덱싱 및 슬라이싱이 가능합니다.
df[df.columns[:25]]

# df의 개인정보에 관한 컬럼만을 색인으로 df를 슬라이싱하고 person_df 변수에 할당
person_df = df[df.columns[:25]]
</code>
</pre>

- columns 삭제
> 컬럼삭제 drop('컬럼명', axis=1)
> del (df['컬럼명'])
> 실제로는 컬럼 및 행도 삭제 가능합니다. axis=0(기본값)
> inplace=True 파라메터를 사용해서 원본값을 변경가능합니다.

<pre>
<code>
# 지울 column의 데이터값이 모두 NaN인지 확인
df['id'].sum(), df['id'].isna()

df['id'].isna().all(), df['member_id'].isna().all(), df['url'].isna().all(), df['desc'].isna().all()

person_df.drop('id', axis=1, inplace=True)
# 열방향

person_df = person_df.drop('id', axis=1)
del person_df['member_id']
person_df.pop('url')
</code>
</pre>

- columns name 변경

<pre>
<code>
# home_ownership을 간략하게 home으로 변경
# 한글도 가능합니다만 권장하지는 않습니다.
person_df.rename(columns={'home_ownership' : 'home'}, inplace=True)
</code>
</pre>

## 데이터 샘플링 및 분석
> 데이터병합, 인덱스편집, 컬럼선택만으로도 불필요한 정보를 삭제하고 새롭게 데이>터셋을 만들 수 있는것을 확인했습니다.
> 위에 학습한 내용도 데이터 샘플링에 속한 내용이지만 지금부터는 데이터셋의 데이>터를 살펴보면서 의미있는 데이터를 추려보도록 하겠습니다.
> **데이터프레임의 기본적인 인덱싱, 슬라이싱, 조건부 샘플링을 조합하면 데이터의 샘플을 확인 하는 과정만으로도 데이터분석이 가능해집니다.**

<pre>
<code>
# 분석에 필요한 데이터프레임을 만들었으니 원본값을 사용하겠습니다. 기존 df에 person_df 값을 덮어 씌웁니다.
df = person_df.copy()

# 분석에 필요한 데이터셋을 생성했다면 파일로도 저장 해둡시다.
df.to_csv('./data/person_df.csv', index=False)
</code>
</pre>

#### 데이터 프레임의 형변환
> 원본 데이터에 Owner, owner 같은 직업이지만 대소문자 구분에 따라 다른 값으로 취
급되는 문제가 있다면
> 대소문자 구분을 없애기 위해 모두 소문자로 데이터값을 변경하겠습니다.
> 소문자 변환 전 혹시모를 int, float 데이터가 있을지 모를 상황에 대비해서 모두 >문자열로 변경해주겠습니다.
> 형변환 함수 astype(데이터타입)

<pre>
<code>
df['emp_title'] = df['emp_title'].astype(str)

# 반복문을 사용한 데이터 변경도 가능
# 하지만 파이썬의 강점을 살리지 못한 코드
for index, job_nm in enumerate(df['emp_title']):
    df['emp_title'][index] = job_nm.lower()
</code>
</pre>


## 배운사람들의 코드, 고오급 python 스킬
> numpy를 학습하면서 브로드캐스팅에 관하여 잠깐 언급했었습니다. 그렇다면 그 파워
풀하다던 브로드캐스팅은 어떻게 사용해야할까요?
> 기타 언어에서는 지원하지 않는 기능이니만큼 파이썬의 특징을 가장 잘 살리는 코드
> **`apply`** 함수를 사용하여 인자로 받는 모든 데이터에 함수를 적용

#### apply 함수로 컬럼에 적용시키는 코드 구조
> df['컬럼명'] = df['컬럼명'].apply(lambda x: func(x) if 조건문)

<pre>
<code>
# 대문자 만드는 함수
# NameError는 try 처리가 안됨
def make_upper(x):
    return x.upper()

# apply() 함수사용 반복이 가능한 데이터구조의 모든 인자에 적용
# lambda 각 인자에 적용할 함수 혹은 연산
df['emp_title'] = df['emp_title'].apply(make_upper)

df['emp_title'] = df['emp_title'].apply(lambda x : x.lower())

# 대소문자 구분을 처리한 값 확인
df['emp_title'].value_counts()
</code>
</pre>

- 기존 value_count 값과 차이가 있음을 확인 할 수 있습니다.
- 제공 된 데이터셋이라도 이와 같은 작은 차이가 있을 수 있습니다.
- 데이터를 꼼꼼하게 살펴볼 수록 디테일한 차이를 만들 수 있습니다.

#### 각 직업별 평균연봉이 궁금하다 groupby
> 엑셀의 pivol table 과 비슷한 기능

<pre>
<code>
df.groupby('emp_title').mean()['annual_inc'].sort_values(ascending=False)

# 위 테이블에서 연간수입 접근
df.groupby('grade').mean()
</code>
</pre>

#### 데이터정렬
> 데이터 재구조화

<pre>
<code>
pd.pivot_table(df,
              index= 'loan_amnt',
              columns= 'grade',
              values= 'int_rate',
              aggfunc= np.mean)
</code>
</pre>

#### 결측치 처리
> 데이터 분석을 위해서는 데이터셋 내에 빈 값이 있는 경우 분석에 방해가 될 수 있>는 여지가 많습니다.
> 모든 결측치를 없애야 하는 것은 아니지만 되도록이면 결측치를 채우는 방법, 혹은 없애는 방법등으로 결측치를 처리합니다.
> 몇가지 예시를 살펴보면서 결측치 처리에 대해 알아봅시다.

- info() 함수는 결측치에 대한 정보도 보여줍니다.
- 컬럼별 isnull() 함수를 사용해도 무방합니다.

<pre>
<code>
df.info()
</code>
</pre>

- 컬럼별 결측치 확인을 위한 isnull()함수 리턴값이 bool 형태로 반환되어 조건부 샘
플링이 가능합니다.

<pre>
<code>
df['emp_title'].isnull().sum()
</code>
</pre>

- 컬럼별 결측치 확인을 위한 isnull()함수 리턴값이 bool 형태로 반환되어 조건부 샘
플링이 가능합니다.

<pre>
<code>
df[df['emp_title'].isnull()]
</code>
</pre>
#### 결측치 채우기

- fillna() 함수로 NaN 값을 dti 컬럼의 평균으로 채우기

<pre>
<code>
df['dti'].fillna(df['dti'].mean(), inplace=True)
</code>
</pre>

- fillna() 함수의 다양한 채우기 방법 파라메터 확인해보기

<pre>
<code>
df['dti'].fillna(method='bfill', inplace=True) # 뒤
df['dti'].fillna(method='ffill', inplace=True) # 앞
</code>
</pre>

#### 결측치 제거

<pre>
<code>
# emp_title 결측치가 있는 샘플 확인
df[df['emp_title'].isnull()]

# 결측치 제거
df.dropna().info()

# view값으로 dropna 결과값 확인
df.dropna(inplace=True)
</code>
</pre>

