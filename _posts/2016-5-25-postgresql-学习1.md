---
layout: post
title: postgresql  学习一
category: 学习
keywords: 学习,2016
---


## 环境配置(ubuntu)

apt-get install postgresql postgresql-contrib

sudo -i -u postgres

createeuser bookuser

createdb book -O bookuser

导入扩展

create  extension cube


## 数据表的创建，插入数据，与联结查询

```


create table countries (                                                  country_code char(2) primary key,
country_name text unique);


insert into countries (country_code , country_name) values(0086 ,'china'); 

insert into countries (country_code , country_name) values(1 ,'canada');

create table cities (name text not null,
postal_code varchar(9) check (postal_code <> ''),
country_code char(2) REFERENCES countries,
PRIMARY KEY (country_code, postal_code));

*check* 容易让人忘记 

insert into cities values ('dj','ddd', '3');

insert into cities values ('dj','ddd', '86');

联结查询

select  cities.*, country_name from cities inner join countries on cities.country_code = countries.country_code;


```

## 总结
creatdb, creatuser 相对sql命令更新友好
postgresql扩展很实用，*注意怎样导入扩展吧!*

check REFERENCES

## 参考

[postgresql](https://help.ubuntu.com/community/PostgreSQL)
[postgresql初级入门](http://www.ruanyifeng.com/blog/2013/12/getting_started_with_postgresql.html)
七周七数据库
