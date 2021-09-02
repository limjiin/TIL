# TD : Database Backup

# hot backup / cold backup : 데이터 베이스 백업 시 환경에 따라서

# logical backup / physical backup : 데이터 베이스 백업하는 방법에 따라서
# logical backup : 데이터를 sql 쿼리문으로 변환해서 저장
# sql 쿼리로 변환하는 시간이 소요 : 느린 백업과 복원
# 시스템 자원을 많이 사용
# 파일용량을 적게 사용
# 데이터 복원시 문제 발생 확인이 쉬움 : 에러가 출력
# OS(예: 리눅스) 호환이 잘됨

# physical backup : 데이터를 바이너리 파일(이진 파일) 그대로 복사해서 저장
# 파일용량 많이 사용
# 문제 발생에 대한 확인 거의 불가
# OS 확인이 잘 안될 수 있음
# 백업과 복원의 속도가 빠름
# 시스템 자원을 적게 사용

# 데이터의 양이 적을 때 > 논리적 백업
# 데이터의 양이 많고 빠른 시간 안에 백업해야 하는 경우 > 물리적 백업

# hot logical backup : backup의 스케쥴을 설정해서 백업(crontab)
# cold physical backup

# workbench > logical backup
# 회사에 관련된 자료를 개발팀에 요청 > .csv

# ctrl + t : 새로운 탭 생성

# summary
# 백업
# hot / cold
## 서비스가 동작이 되는 상태에서 백업 가능
## 단 수정이 일어나 데이터는 백업이 어렵다.
--------------------------
## 서비스가 중단된 상태에서 백업
## 기존 파일과 백업 파일 내용이 동일한다.
# logical / physical
## sql 문자로 백업, 단 복원하는 데 시간이 걸리는 단점
## 에러 확인이 가능
## os 상관 없이 백업 가능
---------------------
## 대용량일 때 유리하고 빠르지만
## 무슨 에러인지 알 수가 없다.
## os 호환이 잘되지 않는다.
# hot logical / cold physical
# 목요일 밤 12 ~ 6시, 수요일 밤 12 ~ 4시
