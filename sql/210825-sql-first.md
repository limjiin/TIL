# TD 
##Set up sql, oracle

##Remind
###SQL문 작성 순서: SELECT(출력) > FROM(테이블 조회) > WHERE(기준) > GROUP BY(그룹화)
###SELF JOIN: 동일 테이블 사이의 조인으로, FROM 절에 동일 테이블이 두 번 이상 나타난다.
  (작성 예시)
  SELECT ALIAS명1.컬럼명
             , ALIAS명2.컬럼명
        FROM 테이블1 ALIAS명1, 테이블2 ALIAS명2
      WEHRE ALIAS명1.컬럼명2 = ALIAS명2.컬럼명1;
###SUBSTR(STD_DE, @, #): @번째 자리 부터 #자리 문자열을 기준
###ROUND(값,*자릿수): 값(소수점, 정수, 날짜 등)에 대해 *자릿수 반올림
###AVG(칼럼명): 칼럼의 평균 값
###ORDER BY ASC/DESC: 데이터를 오름차순/내림차순 정렬
###ROWNUM: SELECT절에 의해 추출되는 데이터(ROW)에 붙는 순번이다. 즉, WHERE절까지 만족 시킨 자료에 1부터 붙는 순번이다. 한편, SELECT 리스트에 ROWNUM을 이용하는 것도 가능하다. ORDER BY를 사용한다면 ORDER BY 반영 후 WHERE절에 붙은 ROWNUM으로 정렬해야 섞이지 않는다. 주로 <, <= 사용하며 >, >= 인 경우 ROWNUM은 동작하지 않는다. 
###IS NULL: 입력값을 확인하여 NULL이면 TRUE를 NULL이 아니면 FALSE를 리턴한다.
###IS NOT NULL: 입력값이 NULL이면 FALSE를 NULL이 아니면 TURE를 리턴합니다.
###CASE WHEN ~ THEN ELSE END 문:
  (작성 예시)
  CASE 컬럼명 | 표현식 WHEN 조건식1 THEN 결과1
                                    WHEN 조건식2 THEN 결과2
                                             	.......
                                    WHEN 조건식n THEN 결과n 
                                   ELSE 결과
             END
###BETWEEN A AND B: A와 B의 값 사이에 있으면 된다. (단, A와 B 값이 포함돔)
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
210825-sql-first.md[+] [unix] (18:22 25/08/2021)                                                   2,1 All
-- INSERT --

~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
210825-sql-first.md[+] [unix] (18:22 25/08/2021)                                                   2,1 All
-- INSERT --

