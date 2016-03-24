---
layout: post
title: python flask-sqlchemy db.relationship说明
category: 学习
keywords: 学习,2016
---




## 总结

**我修改了flasky的5a测试得出**

select immediate joined subquery, dynamic

分类

+ immediate joined subquery 立即的
+ select  选择性加载
+ dynamic 动态加载 在原基础上 filter_by all 等等


## 原始数据


### immediate
    users = db.relationship('User', backref='role', lazy='immediate')

2016-03-24 11:19:45,425 INFO sqlalchemy.engine.base.Engine SELECT roles.id AS roles_id, roles.name AS roles_name
FROM roles
WHERE roles.name = ?
 LIMIT ? OFFSET ?
2016-03-24 11:19:45,425 INFO sqlalchemy.engine.base.Engine ('a', 1, 0)
2016-03-24 11:19:45,426 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.username AS users_username, users.role_id AS users_role_id
FROM users
WHERE ? = users.role_id
2016-03-24 11:19:45,427 INFO sqlalchemy.engine.base.Engine (1,)
2016-03-24 11:19:45,427 INFO sqlalchemy.engine.base.Engine COMMIT


### select
    users = db.relationship('User', backref='role', lazy='select')

role = Role.query.filter_by(name='a').first()
2016-03-24 11:20:33,664 INFO sqlalchemy.engine.base.Engine SELECT roles.id AS roles_id, roles.name AS roles_name
FROM roles
WHERE roles.name = ?
 LIMIT ? OFFSET ?
2016-03-24 11:20:33,664 INFO sqlalchemy.engine.base.Engine ('a', 1, 0)
2016-03-24 11:20:33,665 INFO sqlalchemy.engine.base.Engine COMMIT

print role.users

2016-03-24 11:21:41,823 INFO sqlalchemy.engine.base.Engine ('a', 1, 0)
2016-03-24 11:21:41,824 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.username AS users_username, users.role_id AS users_role_id
FROM users
WHERE ? = users.role_id
2016-03-24 11:21:41,824 INFO sqlalchemy.engine.base.Engine (1,)
[<User u'foo1'>, <User u'foo2'>, <User u'foo3'>, <User u'foo4'>]
2016-03-24 11:21:41,825 INFO sqlalchemy.engine.base.Engine COMMIT


### joined

    users = db.relationship('User', backref='role', lazy='joined')


2016-03-24 11:23:14,407 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2016-03-24 11:23:14,409 INFO sqlalchemy.engine.base.Engine SELECT anon_1.roles_id AS anon_1_roles_id, anon_1.roles_name AS anon_1_roles_name, users_1.id AS users_1_id, users_1.username AS users_1_username, users_1.role_id AS users_1_role_id
FROM (SELECT roles.id AS roles_id, roles.name AS roles_name
FROM roles
WHERE roles.name = ?
 LIMIT ? OFFSET ?) AS anon_1 LEFT OUTER JOIN users AS users_1 ON anon_1.roles_id = users_1.role_id


### dynamic

    users = db.relationship('User', backref='role', lazy='dynamic')

    role = Role.query.filter_by(name='a').first()

    print role.users
    print type(role.users)
    print role.users.filter_by(username='foo1').first()


2016-03-24 11:31:58,396 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2016-03-24 11:31:58,397 INFO sqlalchemy.engine.base.Engine SELECT roles.id AS roles_id, roles.name AS roles_name
FROM roles
WHERE roles.name = ?
 LIMIT ? OFFSET ?
2016-03-24 11:31:58,397 INFO sqlalchemy.engine.base.Engine ('a', 1, 0)
SELECT users.id AS users_id, users.username AS users_username, users.role_id AS users_role_id
FROM users
WHERE :param_1 = users.role_id
<class 'sqlalchemy.orm.dynamic.AppenderBaseQuery'>
2016-03-24 11:31:58,399 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.username AS users_username, users.role_id AS users_role_id
FROM users
WHERE ? = users.role_id AND users.username = ?
 LIMIT ? OFFSET ?
2016-03-24 11:31:58,400 INFO sqlalchemy.engine.base.Engine (1, 'foo1', 1, 0)
<User u'foo1'>
2016-03-24 11:31:58,400 INFO sqlalchemy.engine.base.Engine COMMIT
