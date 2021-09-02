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

# sub query : selece




