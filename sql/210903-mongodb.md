# 동기화 = Replication
# 시작하기 전에 aws에서 인스턴스 (master, slave)를 만들어서 퍼블릭 주소 확보
# 스크립트 입력 시 오타 주의 

# 워크벤치에 2개 생성(master, slave)
# master : SHOW MASTER STATUS
# CREATE DATABASE mydb1;
# show databases;
# use mydb1
# slave :  
##CHANGE MASTER TO MASTER_HOST='13.125.213.230', 
##MASTER_USER='root', 
##MASTER_PASSWORD='rada', 
##MASTER_LOG_FILE='mysqlbin.000001', 
##MASTER_LOG_POS=589;
# master : 
##create table test(
##	user_id int(11) primary key AUTO_INCREMENT,
##	name varchar(30) DEFAULT NULL,
##);

##insert into teat value();

# mongodb
# nosql : 테이블 컬렉션 사이의 관계가 없는 데이터 베이스
# 테이블 > 컬렉션
# 로우, 레코드 > 도큐먼트 
# select 가 느림, insert 가 빠름
# 빅데이터는 많은 데이터를 빠르게 저장 > nosql 
# 자바스크립트 문법을 가져와서 쿼리로 작성합니다. 

# 데이터베이스생성
##use Mongo

# 현재 선택중인 데이터 베이스 확인
##db

#데이터 베이스 목록을 보여줌
##show dbs

#도큐먼트 생성
##use Mongo
##db.user.insert({"name":"peter","age":30})

# CREATE collection
# db.createCollection(name, [option])
# option : capped, autoIndex, size(byte), max(document)
# if db memory over, oldest data delete. and newst data insert
## use Mongo
## db.createCollection("user")
# collection = table
## db.createCollection("info1", {autoIndexId: true}, sapped:true, size: 500, max:5)
## db.createCollection("info2", {autoIndexId: true}, sapped:true, size: 50, max:5)

# create collection
# db.createCollection(name, [option])
# option : capped, autoIndex, size(byte), max(document)
# if db memory over, oldest data delete. and newst data insert
## use Mongo
## db.createCollection("user")
# collection = table
# only create
## db.createCollection("info1", {autoIndexId: true, capped:true, size: 500, max:5})
## db.createCollection("info2", {autoIndexId: true, capped:true, size: 50, max:5})

# create, save
## db.article.insert({"title":"ssac", "content":"mongodb"})

# check collection
## show collections
# collection delete
## db.article.drop()

# CRUD : create
# add document
#colums value
## db.info1.insert({"subject":"python", "level":2})
## db.info1.insert({"subject":"css", "level":1})
## db.info1.insert({"subject":"html", "level":1})

# total add document
# prior data delete, cause setting 'max:5', constraint
## db.info1.insert([
##    {"subject":"ruby", "level":2},
##    {"subject":"java", "level":4},
##    {"subject":"c++", "level":5},
##    {"subject":"js", "level":2},
##    {"subject":"go", "level":4}
##])


# prior data delete, cause setting 50 byte like constraint
## db.info2.insert([
##    {"subject":"ruby", "level":2},
##    {"subject":"java", "level":4},
##    {"subject":"c++", "level":5},
##    {"subject":"js", "level":2},
##    {"subject":"go", "level":4}
##])
    
## db.info.insert([
##    {"subject": "python", "level": 2},
##    {"subject": "css", "level": 1},
##    {"subject": "html", "level": 1},
##    {"subject": "ruby", "level": 2},
##    {"subject": "java", "level": 4},
##    {"subject": "c++", "level": 5},
##    {"subject": "js", "level": 2},
##    {"subject": "go", "level": 4},
##])

# CRUD : READ : find
# find(query, projection)
## db.info.find()
## db.info.find( {level: 2} )    

# function : $lt <, $lte <=, $gt >, $gte >=, $eq = : comparision
## db.info.find( {level: {$lte:2}} )

# $in
## db.info.find({subject:{$in:["java","css"]}})

# logical operater
# $or, $and = all, $not, $nor
## db.info.find({$and: [{subject: "python"}, {level: {$gte:2}}]})

# projection : select colums and show
## db.info.find({}, {_id: false,"level": false})
## db.info.find({}, {_id: false,"level": true})

# sort : 1 : asc, -1: desc
## db.info.find().sort({level:1})
## db.info.find().sort({level:-1})
## db.info.find()

# limit : uppest values
## db.info.find().limit(3)
## db.info.find().limit(3).sort({level:1})

# skip
## db.info.find().skip(3)
## db.info.find().skip(3).limit(4)

# CRUD: update
# update(query, set, option)
# all data setting nessary
## db.info.update(
##     {subject:"java"},
##     {subject:"soss", level:2}
## )
## db.info.find()

# if not include query, add new query in table
## db.info.update(
##    {subject:"less"},
##    {subject:"less", level:3},
##    {upsert:true}
## )

# $set : if not $set with update, delete queryname
## db.info.update(
##     {subject:"ruby"},
##     {level:3}
## )
    
## db.info.find()
   
## db.info.update(
##     {subject:"python"},
##     {$set: {level:3}}
## )

## db.info.update(
##     {subject:"python"},
##     {$set: {level:3}}
## )

# multi option
## db.info.update(
##     {level:2},
##     {$set: {subject:"python"}},
##     {multi : true}
## )

## db.info.find()    
    
    
## db.info.update(
##    {level: 2},
##    {$set: {subject: "python"}}
##)
    
# function
## var pageNotion = function(page, pageBlock){
##    return db.info.find().skiap((page-1)*pageBlock).limit(pageBlock)
## }
## pageNotion(2,3)
