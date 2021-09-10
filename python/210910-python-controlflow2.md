# for 문의 중첩
# i, j, k
for i in range(1,6): # 위에 있는 for문의 순환이 이루어짐
    print(i)
    for j in range(0,3): # 온전히 다 실행이 된 이후에야
        print(i, j)

range(x, y, z)
# x: start point
# y: end point + 1
# z: steps

# 자료구조를 순환하는 for문의 활용(매우 중요)

# 횟수뿐 아니라 구간이 정해져 있는 데이터를 인덱스 넘버도 순환 작업가능
# 실제 분석에서도 가장 많이 사용하는 형태가 됩니다.
test_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# test_list 내부를 순환하면서 i를 정의
for item in test_list:
    print(item * 2)

# 횟수뿐 아니라 구간이 정해져 있는 데이터를 순환하면서도 작업가능
test_list = ['서울', '용산구', '해방촌', '르카페', '재즈', '치즈', '요리']
# enumerate() 함수안의 자료구조의 인덱스와 함께 루프
for index, item in enumerate(test_list):
    print(index, item)
    if index == 4:
        test_list[index] = '시티팝'
test_list

# 횟수뿐 아니라 구간이 정해져 있는 데이터를 순환하면서도 작업가능
# 자료구조 2개를 동시에 순환하면서 작업 가능
test_list1 = ['이름', '사는곳', '사는동네', '좋아하는 카페', '음악', '반려묘', '취미']
test_list2 = ['변치웅', '서울 용산구', '해방촌', '르카페', '재즈', '치즈', '요리']
test_list3 = [1, 2, 3, 4, 5, 6, 7]
for item1, item2, item3 in zip(test_list1, test_list2, test_list3): # 순환하는 자료구조의 갯수는 상관 없으나 변수를 추가해줘야 함.
    print(item1, ':',item2, ':', item3)


# images
# -- OK
# -- NG

for files in images:
    if files == OK:
        new_file_path = file_path + '/OK'
        os.chdir(new_file_path):
            for files 2 in  os.listdir():
                open(files2)
# 상, 하위 폴더 상관 없이 모든 폴더를 돌며, 원하는 값을 가져온다.


# 폴더구조를 순환하는 for문의 활용
import os
for file_nm in os.listdir():
    # print(file_nm)
    # 조건문을 활용해서 폴더 내 원하는 확장자명을 가진 파일만 작업
    if file_nm[-5:] == 'ipynb':
        print(file_nm)
        # 원하는 작업들 나열



# 심플한list comprehension 구문
test_list = [i for i in range(10)]
test_list
# if문이 추가된 리스트 컴프리헨션 구문
# 뒤에 추가되는 if 문이 참일 경우에만 i를 추가한다.
test_list = [i for i in range(10) if i % 2 == 0]
test_list

# dictionary Comperhension
test_dict = {key:val for key, val in zip(test_list1, test_list2)}
test_dict

# while
> - 코드의 무한 반복적인 실행을 위한 반복문
> - 조건식이 참일 경우 실행코드가 무한반복하여 실행 됨
> - 보통은 프로그램을 실행 대기상태로 두거나 입력값을 받는 등의 용도로 사용.(데이터 분석 사용빈도 낮음)

## while문의 구조
>**`while` `조건식` `:`** # 조건식이 참이라면
>>**`실행코드`** # 코드가 무한반복 실행

> `while` 문의 조건식이 참일 경우 무조건 실행되게끔 짜여진 구조.
`while` 문을 사용 할 때에는 반복구문을 어떻게 종료 해야할지 설정해야 함.

# 기본적인 while 구문
# for문과는 달리 조건식을 while 구문 바로 뒤에 적어줌
# while문의 무한루프를 컨트롤 하기위한 변수 설정하고 조건식을 추가하여 코드실행을 컨트롤
a = 0
while True :
    print("무한 반복 중", ':', a)
    a = a + 1
    if a > 10 :
        break

a = 0
while a <= 10 :
    print("무한 반복 중", ':', a)
    a = a + 1

# 1~100까지의 합
# while 문
a = 1
total = 0
while True :
    total += a
    a += 1
    if a == 101:
        break
print(total)

# **try, except(오류처리 혹은 예외처리)**
>**`try`**, **`except`** 구문은 오류 발생가능성이 있는 구문을 처리하거나  
반드시 오류가 발생하는 구문을 감싸 정상적인 프로그램 흐름이 이어질 수 있도록 처리하는 예외처리 구문입니다.

>**`try`** **`:`**  
>> **[처리하고 싶은 코드]**

>**`except`** **`[오류명]`** **`:`**  
>> **[try로 처리하지 못한 작업을 처리하기 위한 코드]**

total = 0
test_list = [1, 2, '3', 4, 5, 6, 7, '5', 9, 10]
try:
    for item in test_list:
        total += item
except TypeError:
    for item in test_list:
        total += int(item)

print(total)


try:
    num_list = []
    for i in range(2):
        num = input('숫자를 입력하세요 : ') # 문자를 입력하여 에러발생
        num = int(num) # 값에러
        num_list.append(num)
        a = num_list[5] # 인덱스에러발생
        b = sum(a) # 타입에러

except ValueError:
    print('문자가 입력되었습니다. 숫자를 다시 입력해주세요.')

except IndexError:
    num_list[-1]
