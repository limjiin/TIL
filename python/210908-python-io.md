# I/O란?
## 프로그램 입장에서 들어오는 모든 데이터를 input, 나가는 모든 데이터를 output이라고 한다.
## 메인 메모리 입장에서 생각하는 들어오고 나가는 모든 데이터에 대해서 I/O 처리라고 부릅니다. (단, CPU와의 소통은 제외)

## 사용자로 부터 키보드로 입력받는 것을 stdin이라고 하며, 사용자에게 다시 모니터로 출력되는 것을 stdout이라고 한다.
## 통상적으로는 Unix 환경(터미널 환경)에서 부르던 용어인데, 프로그래밍에 자주 등장하기 때문에 소개한다.

## 프로그램은 메인 메모리 상에 존재하기 때문에, 스토리지로부터 파일을 불러오는 것도 input이고, 프로그램의 결과를 스토리지에 저장하는 것도 output이다. 이러한 작업을 file I/O로 통칭한다.
## 스토리지와 프로그램 사이의 I/O를 file I/O라고 합니다.

# STDIN / STDOUT (Standard IN, Standard OUT)
## 파이썬은 input()을 통해서 stdin을 사용자로부터 입력받을 수 있다.
## stdin은 무조건 문자열 타입이기 때문에,  type casting을 통해서 다른 데이터 타입으로 바꾸어 사용해야 한다.

## 파이썬은 print()를 통해서 stdout을 사용자에게 출력할 수 있다.

## 이와 같은 표현을 list comprehension이라고 한다.
### L = []
### for x in range(1, 5):
###    L.append(x)
### L

### L = list(range(1, 5))
### L = [x for x in range(1, 5)]
### L

# File I/O
## 파이썬에서는 open()을 이용해서 파일을 손쉽게 열 수 있다.
## open()을 통해 파일을 열고 난뒤엔, close()를 통해서 닫아줘야 한다. ( close를 하지 않으면 jupyter가 계속해서 파일을 점유하고 있게 되어, 시스템 낭비가 일어난다. 자세한 얘기는 생략)
## open() 함수는 다양한 옵션을 제공하지만 기본적으로는 txt파일을 여는 것을 기본으로 가정한다.
## 다른 타입의 파일을 열기 위해선 다른 라이브러리들이 필요하다.
## e.g. csv, excel 파일을 열기 위해 pandas, csv, openpyxl 라이브러리를 사용할 수 있다.
## e.g. png, jpg 파일을 열기 위해 PIL, opencv 라이브러리를 사용할 수 있다.
## e.g. pk, pkl 파일을 열기 위해 pickle 라이브러리를 사용할 수 있다.
## 텍스트 파일을 여는 방법에는 read(), readline(), readlines(), for문을 이용한 방법이 있다. 코드를 통해 각 방법의 차이를 알아보자.

### f.read()를 통해 data 폴더안에 있는 test.txt를 read mode로 열어봅니다.
with open("/Users/user/Downloads/data/test.txt", 'r',  encoding="utf-8") as f:
    data = f.read() 
# f. read 함수는 txt 파일에 있는 모든 글자를 가져와서 하나의 string으로 저장한다.
data

### f.readline()를 통해 data 폴더안에 있는 test.txt를 read mode로 열어봅니다.
with open("/Users/user/Downloads/data/test.txt", 'r',  encoding="utf-8") as f:
    data = f.readline() 
# f.readline 함수는 txt 파일에 있는 첫번째 줄만 가져온다.
data

### f.readlines()를 통해 data 폴더안에 있는 test.txt를 read mode로 열어봅니다.
with open("/Users/user/Downloads/data/test.txt", "r", encoding='utf-8') as f:
    data = f.readlines() 
# f.readlines 함수는 txt 파일에 있는 모든 텍스트를 한줄
data

### for문을 통해 data 폴더안에 있는 test.txt를 read mode로 열어서 출력해봅니다.
with open("/Users/user/Downloads/data/test.txt", "r", encoding='utf-8') as f:
    for line in f:
        print(line)
# f.line 함수는 모든 텍스트를 한줄로, string으로 가져온다.
# 제대로 데이터가 저장되어 있는지, 불러서 확인 가능.

output = []
### test.txt를 read mode로 열고 할 일이 끝나면 자동으로 닫는다.
with open("/Users/user/Downloads/data/test.txt", "r", encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if len(line) > 1:
            output.append(line)
# 한글자 이상인 텍스트만 output list에 저장한다.
output

### result.txt로 output list에 있는 내용을 저장하기 위해 write mode로 열었다.
with open("/Users/user/Downloads/data/test.txt", "w", encoding='utf-8') as f:
    for line in output:
        print(line, file=f)

### OPTIONAL) pickle 라이브러리를 통해서 파이썬 object 자체를 저장하기
import pickle

with open("/Users/user/Downloads/data/test.pk", "wb", encoding="utf-8") as f:
    pickle.dump(output, f)
    
with open("/Users/user/Downloads/data/test.pk", "rb", encoding="utf-8") as f:
    output = pickle.load(f)
