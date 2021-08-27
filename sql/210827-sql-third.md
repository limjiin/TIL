#TD

##SELECT ~, COUNT() CNT: row  수 를 구함
##UPPER(text): text를 대문자로 변환
##CREATE INDEX IDX_테이블명 from 테이블명(값); 데이터 처리 빠르게 만듦
##Ctrl + Shift + E: Index 적용 여부 확인
##테이블 JOIN
##TRUNC(“값”, ”옵션”): 주로 소수점 절사 및 날짜의 시간을 없앨 때 사용한다.
###(작성 예시)
###WITH TEMP AS (SELECT TO_DATE('2018-12-13 22:10:59', 'YYYY-MM-DD HH24:MI:SS') DT, 1234.56 NMB FROM DUAL) 
###SELECT DT 
###     , TRUNC(DT)  --시간 절사
###     , NMB 
###     , TRUNC(NMB) --소수점 절사 
###  FROM TEMP
##SUBSTR(str, pos, len): 문자열을 구하는 값
