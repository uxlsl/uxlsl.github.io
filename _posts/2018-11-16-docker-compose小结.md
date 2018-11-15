---
layout: post
title: docker-compose小结
category: 学习
keywords: 学习,2018
---

# docker-compose小结

官方例子

```yml

version: '3'
services:
  web:
    build: .
    ports:
     - "5000:5000"
  redis:
    image: "redis:alpine"

```


docker-compose的配置文件是yml
配置文件：有三个版本,一般用最新版本3

文件命令参考:https://docs.docker.com/compose/compose-file/

容器互连可以直接通过名字 services: 下面的名子,
必要时使用links,是为了容器名子适应另一个容器

```

version: "3"
services:
    web1:
        image: python
        command: ping web2

    web2:
        image: python
        command: ping web1

```

使用volumes挂载路径

```

version: "3"
services:
    web1:
        image: python
        command: ls /tmp/foo
        volumes:
            - .:/tmp/foo

```

使用ports映射端口

```

version: "3"
services:
    web1:
        image: python:3
        command: python3 -m http.server
        ports:
            - 8000:5678

```

使用environment设置环境变量
