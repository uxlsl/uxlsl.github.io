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

create TABLE countries (
    country_code char(2) primary key,
    country_name text unique);

create TABLE cities (
    name text not null,
    postal_code varchar(9) check (postal_code <> ''),
    country_code char(2) REFERENCES countries,
    PRIMARY KEY (country_code, postal_code));


CREATE TABLE venues(
    venue_id SERIAL PRIMARY KEY,
    name varchar(255),
    street_address text,
    type char(7) CHECK (type in ('public', 'private')) DEFAULT 'public',
    postal_code varchar(9),
    country_code char(2),
    FOREIGN KEY (country_code, postal_code)
       REFERENCES cities (country_code, postal_code) MATCH FULL);

CREATE TABLE events(
    event_id SERIAL PRIMARY KEY,
    title char(64) NOT NULL,
    starts timestamp NOT NULL,
    ends timestamp NOT NULL,
    venue_id integer REFERENCES venues 
);

INSERT INTO countries (country_code , country_name ) values 
('us', 'united states'), ('cn', 'china'), ('mx', 'mexico');

INSERT INTO countries(country_code, country_name) values ('cn', 'china'); 
INSERT INTO cities values('guangzhou', '002', 'cn');

select cities.* ,country_name from cities inner join countries on cities.country_code = countries.country_code;

INSERT INTO venues(name, street_address, postal_code, country_code)
values ('tianhe','hi', '002', 'cn') RETURNING venue_id;

create index events_starts on events using btree (starts);
insert into events (title, starts, ends, venue_id) values('333', '2001-09-28 00:00:00', '2002-09-28 00:00:00', NULL);


```

python使用postgresql例子

```

 import random
 import datetime
 from  timeit import timeit
 import psycopg2
 
 
 def insert_events_data(count):
     vars_list = []
     sql = '''
     insert into events (title, starts, ends, venue_id)
     values(%s, %s, '2016-5-26 00:00:00', 1)
     '''
 
     for i in range(count):
         vars_list.append(
                 [i+1, (datetime.datetime(2001,1,1)
                     + datetime.timedelta(days=random.randint(0, 10000))).            strftime('%Y-%m-%d %H:%M:%S')])
     conn = psycopg2.connect(database='book')
     cur = conn.cursor()
     cur.executemany(sql, vars_list)
     conn.commit()
 
 print(timeit('insert_events_data(10**4)', 'from __main__ import                      insert_events_data', number=10))


```


## 总结
creatdb, creatuser 相对sql命令更新友好
postgresql扩展很实用，*注意怎样导入扩展吧!*
check REFERENCES references
create index events_starts on events using btree (starts);
btree
executemany 

## 参考

[postgresql](https://help.ubuntu.com/community/PostgreSQL)
[postgresql初级入门](http://www.ruanyifeng.com/blog/2013/12/getting_started_with_postgresql.html)
七周七数据库
