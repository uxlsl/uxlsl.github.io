---
layout: post
title: sqlalchemy 觉见问题!
category: 学习
keywords: 学习,2018
---


# create__engine连接字符串问题

'latin-1' codec can't encode characters

这种情况下与系统有关，有时会报有时不会报，笔者曾经在自己linux系统上正常，docker上报这个错

安全写法

+ mysql+pymysql://scott:tiger@localhost/test?charset=utf8mb4&binary_prefix=true
+ postgresql://user:pass@host/dbname?client_encoding=utf8
+ mssql+pyodbc://scott:tiger@myhost:port/databasename?driver=SQL+Server+Native+Client+10.0



# 参考
https://docs.sqlalchemy.org/en/latest/core/engines.html
