---
layout: post
title: docker swarm 小试
category: 学习
keywords: 学习,2018
---


# swarm 集群

Docker Swarm是一个*原生*的Docker集群管理工具。Swarm将一组Docker主机作为一个虚拟的Docker主机来管理。Swarm有一个非常简单的架构，它将多台Docker主机作为一个集群，并在集群级别上*以标准Docker API的形式*提供服务

*注意2375端口*

## 使用dockerHub创建swarm集群, 并且记录下来命名为token_id


```

docker run --rm swarm create

```


## 加入集群

```

docker run -d swarm join --addr=*****:2375 token://$token

```

## 管理集群

```

docker run -d -p 2380:2375 swarm manage token://$token

```


查集群里的节点

```

docker run --rm swarm list token://$token


```

```

docker -H tcp://localhost:2380 info

```

## 运行hello world!

```

docker -H tcp://localhost:2380 run hello-world

```


### 可能碰到问题

+ 在mac环境下2375端口不存在, 可使用socat转发

```

 docker run -it -d --name=socat \
  -p 2375:2375 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  bobrik/socat \
  TCP4-LISTEN:2375,fork,reuseaddr UNIX-CONNECT:/var/run/docker.sock


```


#参考


[dockerd](https://docs.docker.com/engine/reference/commandline/dockerd/)
