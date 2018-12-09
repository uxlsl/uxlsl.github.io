---
layout: post
title: kubernetes入门教程总结
category: 学习
keywords: 学习,2018
---

# kubernetes入门教程总结

1. 创建kubernetes集群
2. 部署应用
3. 访问应用
4. 调节应用
5. 滚动更新


1. 创建kubernetes集群

kubectl get nodes # 说明集群有节点
kuberctl cluster-info # 查看集群信息情况，如master

2. 部署应用

kubectl run kubernetes-bootcamp \
	--image=docker.io/jocatalin/kubernetes-bootcam:v1 --port=8080

类似docker 端口要指定出来，不然出不去

3. 访问应用

kubectl expose deployment/kubernets-bootcamp --type="NodePort" \
	--port 8080

kubectl get services 

4. 调度应用

kubectl get deployments 
kubectl scale deployments/kubernete-bootcamp --replicas=3
kubectl get pods

5. 滚动更新

kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=jocatalin/kubernetes-bootcamp:v2

kubectl get pods


## 参考
**以上均来自官网**

[kubernetes-basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
