---
layout: post
title: 使用kibana的docker版本快速进行数据搜索与分析
category: 学习
keywords: 学习,2018
---

# 使用kibana的docker版本快速进行数据搜索与分析

主要想法

1. 使用python的elastic客户端把数据推向elastic,
2. elastic -> kibana,
3. 然后使用kibana进行分析


## docker-compose.yml

```

version: '3.1'

services:
		//你部分,主要还要写elastic
        depends_on:
            - elastic

    elastic:
        image: docker.elastic.co/elasticsearch/elasticsearch-oss:6.2.4
        container_name: elasticsearch
        environment:
            - bootstrap.memory_lock=true
            - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
        ulimits:
            memlock:
                soft: -1
                hard: -1
        networks:
            - localhost
        ports:
            - 9200:9200
        volumes:
            - ./data/elastic:/usr/share/elasticsearch/data

    kibana:
        image: docker.elastic.co/kibana/kibana-oss:6.2.4
        container_name: kibana
        networks:
            - localhost
        ports:
            - 5601:5601
        environment:
            - ELASTICSEARCH_URL=http://elastic:9200
        depends_on:
            - elastic

networks:
    localhost:

```


python 部分

```

ELASTIC_HOSTS = [
	{
		'host': 'elastic',
		'port': 9200
	},
]
client = Elasticsearch(hosts=ELASTIC_HOSTS)
client.index(
	index='foobar', doc_type='POST', body=dict(item), id=item['id'])

```


## 问题

1. depends_on的作用
控制启动顺序

2. data 的权限问题
data如果为root,要改为其他用户
