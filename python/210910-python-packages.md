# 파이썬 내장 패키지(모듈, 라이브러리, 클래스)

## os
> 파일 및 디렉토리(폴더)관리를 위한 파이썬 내장패키지

### 모듈 import
import os

### 현재 파이썬 커널 경로 확인
path = os.getcwd()
path
### 사용법은 공식 다큐먼트에서 확인하는 것이 가장 정확함

### 경로이동
os.chdir('/Users/user/Downloads/파이썬을 활용한 비즈니스 데이터 분석가/[SSAC] 파이썬_변치웅 강사님')
os.getcwd()

### 현재 파일에 위치한 폴더 리스트 확인
!dir

### 현재 파일 경로 확인
pwd

### 경로 생성
os.mkdir('test')

### 현재 경로 파일, 폴더 리스트
os.listdir()

### 경로 삭제
os.rmdir('test')

### 조건문 활용 파일 셀렉션
for file_nm in os.listdir():
    print(file_nm)

for file_nm in os.listdir():
    if file_nm[-5:] == 'ipynb':
          print(file_nm)

## glob
파일 혹은 폴더 리스트를 관리하기 위한 파이썬 패키지

### 모듈 import
from glob import glob

### glob 함수 적용(os 보다 훨씬 간단해짐)
glob('*.ipynb')

## time, datetime
현재시간, 시간차등 시간 데이터 관리를 위한 파이썬 패키지

### 모듈 import
import time

# time sleep : 입력해준 초만큼 결과 값 딜레이
time.sleep(5)
print('코드 딜레이')

for i in range(10):
    time.sleep(2)
    print('코드 딜레이')

### 모듈 import
from datetime import datetime # as dt

### 현재시간
current_time = datetime.now()

### 현재시간 western 방식으로 출력
current_time.ctime()

### 각 시간 단위 접근
### 함수가 아닙니다.
print(current_time.year)
print(current_time.month)
print(current_time.day)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)
print(current_time.microsecond)

### datetime 데이터 타입을 문자열 형식으로(활용도 높음)
current_str_time = current_time.strftime("%y/%m/%d %H:%M:%S")
### 년, 월, 일, 시, 분, 초
### 요일(%a)

### 문자열 형식의 날짜를 datetime 형식으로
datetime.strptime(current_str_time, '%y/%m/%d %H:%M:%S')

### 이슈나 사건, 로그에 따라서 데이터가 누적이 되는 경우
### 웹페이지 로그 분석
### 유저 1페이지 머무른 시간, 2페이지에 머무른 시간
time_test = current_time2 - current_time
### 시간차 계산

current_time2 < current_time
### 비교 연산 가능함
time_test.seconds

## Text 파일 읽고 쓰기

### 파일을 읽어들이고 작업을 하고 닫는 과정
### 1. 파일을 읽어 들어옴
### 2. 작업을 하고
### 3. 파일을 닫아줘야 함.

### 모드 - 읽기 : r, 쓰기 : w, 추가: a
f = open('test.txt', 'w')
for i in range(10):
    data = f'{i}번째 데이터 입니다.\n' #\t: 탭
    f.write(data)
f.close()
### 파일 닫기
### 닫히는 순간 데이터가 저장됨.

### text.txt 생성됨
f = open('test.txt', 'r')
text_line = f.readlines()
### 저장한 텍스트를 라인별로 가져옴
f.close()
text_line

txt_list = []
for txt in f.readlines():
#    txt_list.append(txt[:-2])
    txt_list.append(txt.replace('\n', ''))
txt_list
