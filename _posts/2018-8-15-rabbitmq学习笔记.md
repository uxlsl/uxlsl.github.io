---
layout: post
title: rabbitmq学习笔记
category: 学习
keywords: 学习,2018
---


# rabbitmq学习笔记

## 常用指令

1. 查绑定rabbitmqctl list_bindings
2. 查队列rabbitmqctl list_queues
3. 查状态rabbitmqctl status


## 交换机

类型: fanout, topic, direct

fanout类型： 发送信息，接收方都能收到
topic类型:  接收方可以选择性接收哪些信息
direct: topic初级版本
