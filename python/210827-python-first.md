#TD

##bins: 가로축 구간의 개수
##range(): 함수의 세번째 인수는 숫자 간의 거리
##figsize = (가로축, 세로축) : 크기
##x축 눈금설정: xticks(설정할 눈금의 위치, 눈금의 이름, 폰트사이즈, 각도)
##x축 범위설정: xlim([-1,4])
##첫 행 삭제:  skiprows=[0]
##결측치 확인 
###열단위: df.isnull().sum()
###행단위: df.isnull().sum(axis=1)
##round(숫자, 반올림할 자릿수): 참고로 '-'는 양수이다.
##shape - dataframe의 크기(행, 열의 수): 구문으로 쓸 때, ()를 사용하지 않는다.
##describe() - 각 열에 대한 기술통계량으로 데이터의 수, 평균, 표준편차, 최소값, 1사분위수, 2사분위수, 3사분위수, 최대값을 나타냄. 
###pandas출력 옵션설정 - float형식으로 수치표기  
###pd.set_option('display.float_format', '{:.2f}'.format)
##columns - 칼럼명 반환, 구문으로 쓸 때, ()를 사용하지 않는다.
##unique() - 열(시리즈)의 고유값
###len()을 사용하면 총 개수를 구할 수 있음
##value_counts() - 열의 고유값 빈도
##sort_values() - 정렬(default : 오름차순), (ascending=false: 내림차순)
##reset_index() - 인덱스 재생성, 기존 인덱스를 데이터프레임의 열로 반환
##inplace(True): 기존 변수에 새로운 변수 적용
##quantile() - 분위수 출력(default : 2사분위수(중앙값))
###소수점 제거 = 실수(float) => 정수(int)로 변경: (columns명).astype(int)
##set_index('키워드'): 데이터프레임의 인덱스를 키워드로 변경
##index - 중점관리키워드 출력
##count() - 각 광고그룹 데이터의 개수
##mean() -각 광고그룹 데이터의 평균
##median() - 그룹 데이터의 중앙값
##std() - 그룹 데이터의 표준편차
##var() - 그룹 데이터의 분산
##concat : 시리즈 혹은 데이터프레임 결합(default-행방향 결합)
##pd.pivot_table('데이터프레임 변수',values=집계 대상 칼럼, index=행 인덱스가 될 칼럼명, columns=열 인덱스가 될 칼럼명, aggfunc=sum)
