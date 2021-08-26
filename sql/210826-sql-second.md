# TD Ch 04. 대중교통 데이터 분석

##데이터 분석 순서: 데이터 다운로드 및 파일명, 폴더 변경 > SQL Developer를 이용하여 DASQL 계정으로 접속 후 테이블 생성 > 테이블에 다운 받은 데이터를 임포트 > DBeaver에서 임포트한 테이블 생성 및 데이터 삽입 > 데이터 삽입 시 데이터 복제를 이용 > 원하는 결과에 맞춰 SQL 구문 작성

##From 절에서 테이블을 조회한 뒤, WHERE을 기준으로, GROUPBY절에서 그룹화한다. SELECT절에서 조회하고, ORDER BY절에서 정렬한다.

##BEGIN_TIME/END_TIME

##ROW NUM
###1) SELECT:  SELECT A.STATN_NO , A.STATN_NM , A.HO_LN , A.NMPR_CNT , ROW_NUMBER() OVER(PARTITION BY A.HO_LN ORDER BY A.NMPR_CNT DESC) AS RN_HO_LN_NMPR_CNT
###2) WHERE: WHERE ROWNUM <= 10;
