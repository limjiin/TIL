# TD

# join, unique, sub query
# view : 가상테이블 : 쿼리를 줄여줄 수 있음
# index : select의 속도를 빠르게 해주는 기능
# trigger : 특정 테이블에 특정 쿼리가 실행될 때, 지정한 쿼리를 실행하는 방법

# create talble 예시
## create table addr(
##	addr_id int primary key auto_increment,
##    addr_name varchar(30) not null,
##    user_id int not null
##);

# drop tabel 테이블명

# inner join: on/where 둘 다 사용 가능하다.
## select user.user_id, user.name, addr.addr_name
## from user
## join addr
## on user.user_id = addr.user_id;

# left join : where 절을 사용할 수 없다.
## select user.user_id, user.name, addr.addr_name
## from user
## left join addr
## on user.user_id = addr.user_id;

# right jon : where 절을 사용할 수 없다.
## select user.user_id, user.name, addr.addr_name
## from user
## right join addr
##on user.user_id = addr.user_id;

#set @RANK = 0;
## select @RANK := @RANK +1 as ranking, country.code, country.Name, country.population
##	, city.name, city.Population
##    , round(city.Population/country.Population * 100,2) as rate
## from country
## join city
## on country.code = city.countrycode
## having city.Population >= 500*10000
## order by rate desc
## limit 10;

# group by 사용 시, group by에 없는 select 함수는 결합함수이어야 한다.

# 테이블 3개 조인
## 국가이름, 도시이름, 사용언어, 사용언어 비율
## use world;
## select country.name as country_name, city.name as city_name, language, percentage
## from country
## join city
## on country.Code = city.countrycode
## join countrylanguage
## on country.Code = countrylanguage.CountryCode;

# Union : 쿼리를 실행한 결과를 row 데이터 기준으로 합쳐서 출력함
# 중복 데이터 제거 효과
# 중복 데이터를 제거하지 않는다면, union all
## select name
## from user
## union
## select addr_name
## from addr;

# Outer join
## select user.user_id, user.name, addr.addr_name
## from user
## left join addr
## on user.user_id = addr.user_id
## union
## select addr.user_id, user.name, addr.addr_name
## from user
## right join addr
## on user.user_id = addr.user_id;

# sub query : 쿼리 안에 쿼리를 사용
# select, from, where

# sub query : selecet
## select (select count(*) from country) as country_count
##	 , (select count(*) from city) as city_count
##     , (select count(distinct(language)) from countrylanguage) as language_count
## from dual ;

# sub query : from
## 800만 이상이 되는 도시의 국가 코드, 도시 이름, 도시 인구수 출력
##(1)
## select country.Code, country.name, city.name, city.population
## from country #239
## join city #4079 > 975000 rows
## on country.code = city.countrycode #4079
## having city.population >= 800*10000; #10

##(2)
## select country.Code, country.name, city.name, city.population
## from (select * from city where population >= 800*10000) as city #10
## join country #239 > 2390 rows
## on country.code = city.countrycode; #10

# sub query : where 
## 800만 이상 도시의 국가코드, 국가이름, 대통령 이름을 출력
## select code, name, headofstate, population
## from country
## where population >= (select population from country where code = "KOR");
## in을 사용하지 않는다면, 조건은 1가지만 가능하다. 

# any : or : 둘 중에 한 가지만 만족해도 true 
# all : and : 둘 다 만족해야 true
## select code, name, headofstate, population
## from country
## where population >= any(
## 	select population from country where code in ("KOR", "BRA")
##    );

## select code, name, headofstate, population
## from country
## where population >= all(
##	select population from country where code in ("KOR", "BRA")
##    );

# view
# 가상의 테이블로 특정 쿼리를 실행한 결과 데이터를 출력하는 용도
# 실제 데이터를 저장 X > 수정 및 인덱스 설정이 불가능
# 쿼리를 조금 더 단순하게 작성하게 해주는 기능
# 특정 컬럼의 데이터 테이블이 수정되면 뷰 테이블도 같이 수정됨 

## 800만 이상의 도시 인구가 있는 국가의 국가코드, 국가이름, 도시이름
## create view city2 as
## select countrycode, name 
## from city 
##where population >= 800*10000;

## select country.code, country.name, city2.name
## from city2 
## join country
## on country.code = city2.countrycode;

# index : 데이터 검색을 빠르게 찾을 수 있도록 도와주는 기능
# select, where 절에 사용할 때 빠름
# insert, delete, update 할 때는 속도가 느려짐 
## show index from salaries;
## select count(*) from salaries;
## desc salaries;
## create index tdate on salaries (to_date);
## select * from salaries where to_date < "1986-01-01";

# 실행계획 : explain
## explain
## select * from salaries where to_date < "1986-01-01";
## rows, filtered : 예측 값, 실제 값하고는 다름.

# trigger : 특정 테이블을 감시하고 있다가 설정한 조건이 감지되면 지정해놓은 쿼리가 자동으로 실행
## 쿼리의 시작과 끝을 |로 설정하겠다.
## 한줄 한줄 삭제될 때
## delimiter |
## 	create trigger backup_tr
##	before delete on chat
##	for each row begin  
##		insert into backup(backup_msg)
##		values (old.msg);
## end |
## show triggers;

