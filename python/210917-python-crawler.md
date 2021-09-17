# **데이터 크롤링**

## **크롤링이란?**
> 크롤러(crawler)는 자동화된 방법으로 웹을 탐색하는 컴퓨터 프로그램  
> '웹 크롤링'(web crawling)??  
> '데이터 크롤링'(data crawling)!!  
> 구글링, 네이버 검색 등

## **웹 크롤링**
> 웹 서비스 내 정보를 수집하는 일
> 필요한 정보가 있다면?
> API 확인 -> 없으면 직접 크롤링
> 다만 서비스 제공자의 입장에서는??

### 웹 **서핑**을 하는 의식의 흐름
> 브라우저 오픈  
> 원하는 인터넷페이지 주소 입력  
> 화면이 열리면 찾고자 하는 정보를 스크롤 하면서 찾기  
> 문자, 그림, 동영상 조회  

### 웹 **크롤링** 하는 의식의 흐름
> 정보를 가져오고자 하는 url 정의
> url 정보로 requests로 정보 요청
> text 정보를 html로 변환
> html에서 우리가 필요한 정보만 선별

### 웹 크롤링을 위해 BeautifulSoup 사용
> requests는 요청을 받기는 하지만 text로만 받음  
> API는 통신을 위해 정형화 된 데이터 형태의 text  
> 우리가 원하는 데이터로 가공하기 위해 편의상 html로 변환  
> text를 html로 변환하는 모듈이 beautifulSoup

[https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### 간단한 데이터 크롤링으로 기본 개념잡기

<pre>
<code>
# 필요패키지 import
import numpy as np
import pandas as pd
import requests # 크롤링에 사용하는 패키지
from bs4 import BeautifulSoup # html 변환에 사용함

# url정의
url = 'https://naver.com'

# requests로 url에 정보요청
response= requests.get(url)

# 정리되지 않은 정보
response.text

# 정보를 html 변환 (보기 쉽게)
html = BeautifulSoup(response.text, 'html.parser')

# html 내에서 우리가 보고 싶은 정보만 선별
html.select('img')

# 다음 뉴스 페이지 크롤링
url1 = 'https://www.daum.net/'

response = requests.get(url1)

html1 = BeautifulSoup(response.text, 'html.parser')

html1.select('img')
</code>
</pre>

### 실제 개발자가 작성한 코드로 확인된다
> 정제되지 않은 데이터로 가독성이 좋지 않음  
> 우리는 이 중에서 우리가 원하는 정보를 선별해서 가져오는 작업을 진행합니다.  
> 그러기에 html의 기본 구성을 살펴보도록 하겠습니다.  

#### 웹 페이지의 구성
> **HTML(Hyper Text Markup Language)**  
> www 를 구성하는데 사용하는 국제표준 언어로서 컨텐츠와 레이아웃을 담고 있다

> **<태그>** 내용 **</태그>**  
<tag이름 class="class이름1 class이름2" id="주민번호" href="주소"></tag이름>

> 형태나 속성을 묘사하기 위한 구조적 언어 : HTML, CSS (계층이 있음)  
> 웹의 작동 및 제어를 위한 프로그래밍 언어 :  Js

#### 셀렉터
> 용도 : html에서 내가 원하는 내용을 찾아내기 위해서  
<span class="news" id="1234">비비고 왕교자</span>

- 단일 셀렉터  
> html.select('span') # 태그 이름이 span인 친구들 다 들고 옴  
> tag : span  
> class(별명, 그룹명) : .news  

- 클래스 포함 셀렉터  
> html.select('span.news')

- id 포함 셀렉터  
> id(고유값) : #1234  
> html.select('span#1234')

#### 복합 셀렉터
    1. 조합 셀렉터
    <span>1</span>
    <span class="txt">2</span>
    <em class="txt">3</em>
    
    태그 이름이 span이고 클래스 이름은 txt인 라인을 찾고 싶다. : span.txt 
    li 태그 중에서 id가 name 인 라인을 찾고\ 싶다. : li#name

    2. 경로 셀렉터
    <ul>
        <li><span>이걸 찾으려면?</span></li>
    </ul>
    <span>이건 아님</span>

    ul 태그안 li 태그 안 span 라인을 찾는다
    ul > li > span 혹은 ul li span

<pre>
<code>
# 슬의생 드라마 크롤링
url2 = 'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%8A%AC%EC%9D%98%EC%83%9D'

response = requests.get(url2)

html2 = BeautifulSoup(response.text, 'html.parser')

html2.select('dd.cont')[0].text

for con in html2.select('dd.cont'):
    print(con.text)

# 슬의생 기사 크롤링
for title in html2.select('a.fn_tit_u')[1:]: #a.tit_main, fn_tit_n
    print('-'*20)
    print(title.text)

# 3개 이상의 드라마 크롤링
import time

dr_nm = ['도깨비', '호텔델루나', '슬기로운의사생활']

# name = input('제목을 입력해주세요 : ')

for name in dr_nm:
    # 순환은 빠르다
    print('-'*20)
    print(f'{name} 크롤링 중입니다.')
    url3 = f'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q={name}'

    # 초당 40~50회 요청
    # 다음에서 기계가 요청하는구나 막힘

    # 차단막는 코드
    seed = np.random.randint(100) # 시드도 난수로 만들고
    np.random.seed(seed) # 시드 생성
    a = np.random.randint(5) # 시드에서 난수 생성
    time.sleep(a)

    response = requests.get(url3)

    html3 = BeautifulSoup(response.text, 'html.parser')

    print(html3.select('dd.cont')[0].text)
print('크롤링 종료')
</code>
</pre>

## 다음에서 로또번호 가져오기

- 로또 번호 1개 가져오기

<pre>
<code>
# url 설정
url5 = 'https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=980%ED%9A%8C+%EB%8B%B9%EC%B2%A8+%EB%B2%88%ED%98%B8'

# requests로 데이터 요청하기
response = requests.get(url5)

# html로 변환
html5 = BeautifulSoup(response.text, 'html.parser')

html5.select('span.ball')

ball_num = []
for ball in html5.select('span.ball')[:-2]:
    ball = ball.text
    ball_num.append(ball)
ball_num
</code>
</pre>

- 전체 로또 번호 가져오기

<pre>
<code>
total_lotto = []

for i in range(680, 981):
    print('-'*20)
    print(f'{i}회차 당첨번호 크롤링 중입니다.')
    url5 = f'https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={i}회차+당첨+번호'

    # 차단막는 코드
    seed = np.random.randint(100) # 시드도 난수로 만들고
    np.random.seed(seed) # 시드 생성
    a = np.random.randint(5) # 시드에서 난수 생성
    time.sleep(a)

    # requests로 데이터 요청하기
    response = requests.get(url5)

    # html로 변환
    html5 = BeautifulSoup(response.text, 'html.parser')

    lotto = []
    for ball in html5.select('span.ball')[:-2]:
        lotto.append(ball.text)
    total_lotto.append(lotto)

print('크롤링이 종료되었습니다.')
</code>
</pre>

- 로또 번호 그래프 만들기

<pre>
<code>
lotto_array = np.array(total_lotto)

lotto_array.shape

# 1열로 만들어줌
lotto_array.reshape(-1, ).shape

# countplot으로 만들기
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(15, 15))
sns.countplot(lotto_array.reshape(-1, ))

# 저장하기
df = pd.DataFrame(total_lotto)
df.to_csv('total_lotto.csv')
</code>
</pre>

### 웹 크롤링 에러 코드

- 100 : 우리 이런정보 내주는거야
- 200 : 성공
- 300 : 우리 이 사이트 이리루 이사했어 일루가
- 400 : 유저가 요청을 잘못한경우
- 500 : 서버 문제

<pre>
<code>
requests.codes.ok
</code>
</pre>

<pre>
<code>
# 차단막는 코드
seed = np.random.randint(100)
np.random.seed(seed)
a = np.random.randint(5)
</code>
</pre>

## **네이버 키워드로 검색한 결과를 크롤링**

<pre>
<code>
key_word = input('키워드를 입력하세요 : ')
url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={key_word}'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')
for name in html.select('a.api_txt_lines'):
    print(name.text, name.attrs['href'])

    temp_url = name.attrs['href']
</code>
</pre>
