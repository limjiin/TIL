# TD summary

## datatype : int, float, double, char, varchar, text, datetime, timestamp

## constraint : not null, unique, primary key, auto_increment, foreign key

## foreign key : 무결성을 제약하는 조건  : on update, on delete

## DDL : CREATE(database, table), ALTER(수정), DROP
### column ADD
#### alter table user2 add tmp text;
### column Modify
#### alter table user2 modify column tmp int;
### column Drop
#### alter table user2 drop tmp;
### table 인코딩 확인
#### show full columns from user2;
### table 인코딩 변경
#### alter table user2 convert to character set ascii;
#### alter table user2 convert to character set utf8;

## DML : CRUD : CREATE(INSERT), READ(SELECT), UPDATE(UPDATE: 데이터를 수정할 때 사용하는 쿼리), DELETE(DELETE)

## FUNCTION : ceil, round, truncate, date_format, concat, count

## if, ifnull, case when then 

## group by, having

### 외래키로 참조 되고 있는 데이터는 삭제할 수 없다.

## on delete, on update 설정
### 참조되는 데이터를 수정, 삭제할 때 참조하는 데이터를 어떻게 처리할지를 설정하는 방법
## cascade : 참조되는 테이블 데이터를 삭제, 수정하면 참조하는 테이블 데이터도 삭제, 수정한다.
## set null : 참조하는 데이터 null 값으로 변경
## no action : 참조하는 데이터를 변경하지 않는다. 
## set default : 참조하는 데이터를 칼럼의 default 값으로 변경이 된다. 
## restrict : 참조하는 데이터를 삭제하거나 수정할 수 없다. 

