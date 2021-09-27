## 네이버 주식 시세 데이터 크롤링

# 동적페이지의 숨은 URL
# 동적 페이지에 요청을 할 때 정책에 필요한 정보를 같이 전달해줘야 함

url = 'https://finance.naver.com/item/sise_day.naver?code=035720&page=1'

info = {
    'referer' : 'https://finance.naver.com/item/sise_day.naver?code=035720&page=1',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

response = requests.get(url, headers=info)

html = BeautifulSoup(response.text, 'html.parser')

# 전체 데이터 tah
# 날짜 p10
html.select('span.p10') # p10 gray03

# 날짜 인덱스 살려서 활용하기
index = [date.text for date in html.select('span.p10')]

price = np.array([price.text.strip() for price in html.select('span.p11')]).reshape((-1, 6))

# 컬럼 정보에 해당하는 데이터 가져오기
columns= [col_name.text for col_name in html.select('th')]

df = pd.DataFrame(total_data,
                 index = index,
                  columns = columns)
df

def remove_str(x):
    return x.replace(',', '')

# 함수 적용
df['종가'] = df['종가'].apply(remove_str)
df

# 타임 변환
df['종가'] = df['종가'].astype(int)

# 그래프 만들기
df['종가'].sort_index().plot()

# np.array로 만들기
total_data = np.array([item.text.strip() for item in html.select('span.tah')]).reshape((-1, 7))
total_data

# for 문으로 만들기
item_list = []
for item in html.select('span.tah'):
    item_list.append(item.text.strip())
item_array = np.array(item_list).reshape((-1, 7))
item_array

## 총 20페이지 주가 정보 크롤링 해서 증가 그래프 출력

info = {
    'referer' : f'https://finance.naver.com/item/sise_day.naver?code=035720',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}


index = []

total_data = np.array([])

for i in range(1, 21):
    
    seed = np.random.randint(100) # 시드도 난수로 만들고
    np.random.seed(seed) # 시드 생성
    a = np.random.randint(5) # 시드에서 난수 생성
    time.sleep(a)
    
    url = f'https://finance.naver.com/item/sise_day.naver?code=035720&page={i}'
    
    # requests 요청 시 헤더 정보 추가
    response = requests.get(url, headers=info)
    
    # html 변환
    html = BeautifulSoup(response.text, 'html.parser')
    
    # 날짜 인덱스 살려서 활용하기
    for date in html.select('span.p10'):
        index.append(date.text)
    
    # 가격정보 추출
    price = np.array([price.text.strip() for price in html.select('span.p11')]).reshape((-1, 6))
    total_data = np.append(total_data, price).reshape((-1, 6))
    
    # 컬럼 정보에 해당하는 데이터 가져오기
    columns = [col_name.text for col_name in html.select('th')[1:]]
    
    print(f'{i}번째 크롤링 중입니다.')
    
    # 데이터프레임 제작
df = pd.DataFrame(total_data,
             index = index,
             columns = columns
df

def remove_str(x):
    return x.replace(',', '')

df['종가'] = df['종가'].apply(remove_str)
df['종가'] = df['종가'].astype(int)
df['종가'].sort_index().plot()

## **관심 있는 개별 종목의 시가총액, 외국인 소진률, PER, PBR**

# url 정의
# 002020 = 코오롱
# 005930 = 삼성전자
# 035720 = 카카오
code = '035720'
url = f'https://finance.naver.com/item/main.naver?code={code}'

# requests 요청
response = requests.get(url)

# html 변환
html = BeautifulSoup(response.text, 'html.parser')

# 데이터 선별
print('시가총액 : ', html.select('em#_market_sum')[0].text.strip())
print('외국인 소진률 : ', html.select('div.gray em')[2].text)
print('PER : ', html.select('em#_per')[0].text)
print('PBR : ', html.select('em#_pbr')[0].text)

import time

stock_list = ['005930', '002020', '323410']
total_data = []

for code in stock_list:
    time.sleep(np.random.randint(5))
    url = f'https://finance.naver.com/item/main.naver?code={code}'
    print(f'{code} 크롤링 중입니다.')

    # requests 요청
    response = requests.get(url)

    # html 변환
    html = BeautifulSoup(response.text, 'html.parser')
    stock_data = []
    stock_data.append(html.select('em#_market_sum')[0].text.strip().replace('\n', '').replace('\t', ''))
    stock_data.append(html.select('div.gray em')[2].text)
    stock_data.append(html.select('em#_per')[0].text)
    stock_data.append(html.select('em#_pbr')[0].text)
    total_data.append(stock_data)

print('크롤링 종료')

totla_data

df = pd.DataFrame(total_data,
                 index=['버킷스튜디오', 'SK하이닉스', '데브시스터즈'],
                 columns=['시가총액', '외국인소진률', 'PER', 'PBR'])
df

## 네이버 데이터랩 인기검색어 크롤링

url = 'https://datalab.naver.com/shoppingInsight/getKeywordRank.naver'

info = {
    'referer' : 'https://datalab.naver.com/',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

response = requests.post(url, headers=info)

import json

data = json.loads(response.text)

data[0]

for item in data[0]['ranks']:
    print(item['keyword'])

## 다음 주식 일자별 주가 데이터 크롤링

url = 'https://finance.daum.net/api/quote/A002020/days?symbolCode=A002020&page=1&perPage=10&pagination=true'

info = {
    'referer' : 'https://finance.daum.net/quotes/A002020',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

response = requests.get(url, headers=info)

response.text

data = json.loads(response.text)

# json 파싱 함수
from pandas.io.json import json_normalize

df = pd.DataFrame(data['data'])
df

## 파파고 API

url = "https://openapi.naver.com/v1/papago/n2mt"

info = {
    "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Naver-Client-Id" : "jqRNFpaeC_H1CK1avZRq",
    "X-Naver-Client-Secret" : "WPIGbWh757"
}

data = {
    'source' : 'ko',
    'target' : 'en',
    'text' : '만나서 반갑습니다.'
}

response = requests.post(url,headers=info, data=data)
response.text

result = json.loads(response.text)
result

result['message']['result']['translatedText']

### 자동으로 한국어를 영어로 출력하기
def papago():

    x = str(input('번역이 필요한 한국어를 입력하세요 : '))
    # url 설정
    url = "https://openapi.naver.com/v1/papago/n2mt"

    info = {
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Naver-Client-Id" : "jqRNFpaeC_H1CK1avZRq",
        "X-Naver-Client-Secret" : "WPIGbWh757"
    }

    data = {
        'source':'ko',
        'target':'en',
        'text': x
    }

    response = requests.post(url, headers=info, data=data)
    result = json.loads(response.text)
    print(result['message']['result']['translatedText'])

[https://developers.naver.com/main/](https://developers.naver.com/main/)

## 공공데이터

url = 'http://smarttour.junggu.seoul.kr//junggu/openapi/culture.do'

response = requests.get(url)

data = json.loads(response.text)

for i in range(i):
    print(data['spot_Data'][i]['spot_Address'][1])

[https://www.data.go.kr/index.do](https://www.data.go.kr/index.do)
