https://kubernetes.io/zh/

http://docs.kubernetes.org.cn/

https://blog.csdn.net/qq_33313357/article/details/123274532

https://blog.csdn.net/qq_40694671/article/details/122529672


# 1. kubectl version
查看client和server的版本信息：
```
kubectl version
```

# 2. kubectl get

## 2.1、kubectl get nodes

### 2.1.1、获取所有节点的信息：
```
kubectl get nodes
```

### 2.1.2、获取某个节点的信息
```
kubectl get nodes <node-name>
```

### 2.1.3、获取某个节点的详细信息：
```
kubectl get nodes <node-name> -o wide
```

### 2.1.4、获取节点的标签：
```
kubectl get nodes <node-name> --show-labels
```

### 2.1.5、给节点打标签：
```
kubectl label nodes node1 disktype=ssd
```
例子中的意思是为node1添加一个key为disktype和value为ssd的label

## 2.2、kubectl get pods

### 2.2.1、获取所有Pod的信息：
```
kubectl get pods
```

### 2.2.2、获取某个Pod的信息：
```
kubectl get pods <pod-name>
```

### 2.2.3、显示某个Pod更多的信息，例如Node IP等：
```
kubectl get pods <pod-name> -o wide
```

### 2.2.4、以YAML格式显示Pod的详细信息：
```
kubectl get po <pod-name> -o yaml
```

### 2.2.5、筛选符合条件的Pod的信息：
```
kubectl get po | grep <XXX>
```
本命令的意思是筛选出含有XXX关键字的所有pod-name的信息

### 2.2.6、导出指定pod的yaml配置：
```
kubectl get pods <指定的pod-name> -o yaml > xx.yaml
```
导出指定的pod的yaml配置，并保存到当前目录，命名为xx.yaml

## 2.3、kubectl get services & kubectl get svc

### 2.3.1、显示所有service的信息：
```
kubectl get services
kubectl get svc
```

### 2.3.2、显示某个service的信息：
```
kubectl get services <service-name>
kubectl get svc <service-name>
```

### 2.3.3、显示某个service更多的信息，例如SELECTOR等：
```
kubectl get services <service-name> -o wide
kubectl get svc <service-name> -o wide
```

### 2.3.4、以YAML格式显示service的详细信息：
```
kubectl get services <service-name> -o yaml
kubectl get svc <service-name> -o yaml
```

### 2.3.5、筛选符合条件的service的信息：
```
kubectl get services | grep <XXX>
kubectl get svc | grep <XXX>
```

### 2.3.6、导出指定service的yaml配置：
```
kubectl get services <service-name> -o yaml> xx.yaml
kubectl get svc <service-name> -o yaml> xx.yaml
```
导出指定的service的yaml配置，并保存到当前目录，命名为xx.yaml

## 2.4、kubectl get ReplicaSets & kubectl get rs

### 2.4.1、显示所有ReplicaSet的信息：
```
kubectl get ReplicaSets
kubectl get rs
```

### 2.4.2、显示某个ReplicaSet的信息：
```
kubectl get ReplicaSets <ReplicaSet-name>
kubectl get rs <ReplicaSet-name>
```

### 2.4.3、显示某个ReplicaSet更多的信息，例如CONTAINERS,IMAGES,SELECTOR等：
```
kubectl get ReplicaSets <ReplicaSet-name> -o wide
kubectl get rs <ReplicaSet-name> -o wide
```

### 2.4.4、以YAML格式显示ReplicaSet的详细信息：
```
kubectl get ReplicaSets <ReplicaSet-name> -o yaml
kubectl get rs <ReplicaSet-name> -o yaml
```

### 2.4.5、筛选符合条件的ReplicaSet的信息：
```
kubectl get ReplicaSets | grep <XXX>
kubectl get rs | grep <XXX>
```

### 2.4.6、导出指定ReplicaSet的yaml配置：
```
kubectl get ReplicaSet <ReplicaSet-name> -o yaml> xx.yaml
kubectl get rs <ReplicaSet-name> -o yaml> xx.yaml
```
导出指定的ReplicaSet的yaml配置，并保存到当前目录，命名为xx.yaml

## 2.5、kubectl get deployments & kubectl get deploy

### 2.5.1、显示所有deployment的信息：
```
kubectl get deployments
kubectl get deploy

```

### 2.5.2、显示某个deployment的信息：
```
kubectl get deployment <deployment-name>
kubectl get deploy <deployment-name>
```

### 2.5.3、显示某个deployment更多的信息，例如CONTAINERS,IMAGES等：
```
kubectl get deployments <deployment-name> -o wide
kubectl get deploy <deployment-name> -o wide
```

### 2.5.4、以YAML格式显示deployment的详细信息：
```
kubectl get deployments <deployment-name> -o yaml
kubectl get deploy <deployment-name> -o yaml
```

### 2.5.5、筛选符合条件的deployment的信息：
```
kubectl get deployments | grep <XXX>
kubectl get deploy | grep <XXX>
```

### 2.5.6、导出指定deployment的yaml配置：
```
kubectl get deployments <deployment-name> -o yaml> xx.yaml
kubectl get deploy <deployment-name> -o yaml> xx.yaml
```
导出指定的deployment的yaml配置，并保存到当前目录，命名为xx.yaml

# 3、kubectl label

## 3.1、给一个pod打一个没有存在的标签key=value：
```
kubectl label pod <pod-name> key=value
```

## 3.2、给一个pod中已经存在的标签重新赋值：
```
kubectl label pod <pod-name> key=value --overwrite
```

## 3.3、通过key删除标签
```
kubectl label pod <pod-name> key-
```

# 4、kubectl describe

## 4.1、查看node的详细信息
```
kubectl describe nodes <node-name>
```

## 4.2、查看Pod的详细信息
```
kubectl describe pods <pod-name>
```

## 4.3、查看service的详细信息：
```
kubectl describe services <service-name>
kubectl describe svc <service-name> 
```

## 4.4、查看ReplicaSet的详细信息：
```
kubectl describe ReplicaSet <ReplicaSet-name>
kubectl describe rs <ReplicaSet-name>
```

## 4.5、查看deployment的详细信息：
```
kubectl describe deployments <deployment-name>
kubectl describe deploy <deployment-name>
```

# 5、kubectl delete

## 5.1、删除node，pod，service，replicaset，deployment
```
kubectl delete node <node-name>
kubectl delete pod <pod-name>
kubectl delete service <service-name>
kubectl delete replicaset <replicaset-name>
```

## 5.2、批量删除含有某些符合规则的pod等，比如：

### 5.2.1、批量删除状态为error的pods，且这几个pod的名字都包含一个test关键字
```
kubectl get pods | grep test | grep error | awk '{print $1}' | xargs kubectl delete pod
```
### 5.2.2、批量删除状态为Evicted的pods，且这几个pod的名字都包含一个test1关键字
```
kubectl get pods | grep test1 | grep Evicted | awk '{print $1}' | xargs kubectl delete pod
```

## 5.3、删除基于xxx.yaml定义的名称，与kubectl apply,kubectl create对应。
```
kubectl delete -f xxx.yaml
```

# 6、kubectl run

用法：
```
kubectl run NAME --image=image [–env=“key=value”] [–port=port] [–replicas=replicas] [–dry-run=bool] [–overrides=inline-json] [–command] – [COMMAND] [args…] [options]
```

创建一个镜像为MYSQL，副本为1，暴露端口为3306的mysql容器：
```
kubectl run musql --image=MYSQL --replicas=1 --port=3306
```

# 7、kubectl create

## 7.1、通过yaml文件配置来创建资源对象：
```
kubectl create -f XXX.yaml
```

## 7.2、创建namespace
用法：
```
kubectl create namespace NAME [–dry-run] [options]
```
如：
```
kubectl create namespace XXX
```

## 7.3、创建secret

用法：kubectl create secret [flags] [options]

### 7.3.1、创建一个TLS Secret
```
kubectl create secret tls tomcat-ingress-sercret --cert=tls.crt --key=tls.key 
kubectl get secrets 
kubectl describe secrets tomcat-ingress-sercret
```

### 7.3.2、创建一个generic Secret
```
kubectl create secret generic mysql-root-password --from-literal=password=xxx
kubectl get secrets 
```

## 7.4、创建configmap
用法：kubectl create configmap NAME [–from-file=[key=]source] [–from-literal=key1=value1] [–dry-run] [options]
```
kubectl create configmap nginx-config --from-literal=nginx_port=80 --from-literal=server_name=myapp.ydt.com
```

## 7.5、创建serviceaccount
```
kubectl create serviceaccount admin
kubectl create serviceaccount sa -o yaml --dry-run
```

# 8、kubectl exec

```
kubectl exec -it <pod-name> bash
```

# 9、kubectl edit

编辑服务器上定义的资源。如果在更新资源时报错，将会在磁盘上创建一个临时文件来记录。在更新资源时最常见的错误是几个用户同时使用编辑器更改服务器上资源，发生这种情况，你需要将你的更改应用到最新版本的资源上，或者更新保存的临时副本。

用法：kubectl edit (RESOURCE/NAME | -f FILENAME) [options]，编辑资源清单

```
kubectl edit pods <pod-name> -o yaml
```

# 10、kubectl apply

把写好的yaml文件发布到kubernetes集群中：
```
kubectl apply -f XXX.yaml
```

# 11、kubectl logs

## 11.1、打印Pod容器中的日志
```
kubectl logs <pod-name>
```

## 11.2、打印Pod容器中的日志的最后N行
```
kubectl logs <pod-name> --tail=N
```

## 11.3、打印Pod容器中，最近10分钟的日志
```
kubectl logs <pode-name> --since=10m
```

## 11.4、持续不断地输出日志，直至按下ctrl+c停止
```
kubectl logs <pod-name> -f
```

## 11.5、保存该pod的日志
```
kubectl logs <pod-name> > podname.log
```

# 12、kubectl explain

用法：kubectl explain RESOURCE [options]，显示各种资源清单的字段解释
## 12.1、查看pod资源清单字段
```
kubectl explain pod
```

## 12.2、查看pod资源清单理apiVersion字段下的字段（以此类推）
```
kubectl explain pod.apiVersion
```

# 13、kubectl roolout

用法：kubectl rollout SUBCOMMAND [options]，滚动更新
类型：
    deployments
    daemonsets
    statefulsets
## 13.1、查看deployment滚动更新历史版本
```
kubectl rollout history deployment （容器名不加后缀 ）-n pred
```

## 13.2、回滚到指定版本
```
#回滚到上一个版本
kubectl rollout undo deployment (容器名)
#显示全部版本号
kubectl rollout history deployment （容器名不加后缀 ）-n pred
#指定回滚的版本
kubectl rollout undo deployment （容器名不加后缀 ） --to-revision=1（1代表版本号）
```

## 13.3、更新一个pod后暂停更新
```
#暂停更新
kubectl rollout pause deployment （容器名）
#显示更详细的
kubectl get pods -l app=（容器名) -w
```

## 13.4、解除暂停状态，继续更新
```
#恢复更新状态
kubectl rollout resume deployment (容器名) 
#监控deployment更新状态
kubectl rollout status deployment （容器名）
```

# 14、kubectl patch

## 14.1、修改deployment副本数
```
kubectl patch deployment (容器名) -p '{"spec":{"replicas":5}}'
```

## 14.2、修改deployment滚动更新策略
```
kubectl patch deployment （容器名） -p '{"spec":{"strategy":{"rollingUpdate":{"maxSurge":1,"maxUnavailable":0}}}}'
kubectl describe deployments (容器名不加后缀)
```

# 15、kubectl set

用法：kubectl set image (-f FILENAME | TYPE NAME) CONTAINER_NAME_1=CONTAINER_IMAGE_1 … CONTAINER_NAME_N=CONTAINER_IMAGE_N [options]

## 15.1、更新现有的资源对象的容器镜像
```
kubectl set image
```

## 15.2、输入关键字查找项目名称
```
kubectl get pod -n prod |grep website（关键字）
```

## 15.3、查看项目详细信息
```
kubectl describe pods -n prod （项目名称）
```

# 16、kubectl scale

kubectl scale用于横向扩展，扩容或缩容 Deployment、ReplicaSet、Replication Controller或Job 中Pod数量。

scale可以指定多个前提条件，如：当前副本数量–current-replicas或资源版本–resource-version，进行伸缩比例设置前，系统会先验证前提条件是否成立。

## 16.1、将deployment的副本数设置为3
```
kubectl scale deployments/<deployment-name>  --replicas=3
```

## 16.2、将xxx.yaml配置文件中指定的资源对象和名称标识的pod副本数设为3
```
kubectl scale --replicas=3 -f xxx.yaml
```

## 16.3、 如果名为xxx的deployment的当前的副本数为2, 需要把它扩增为3
```
kubectl scale --current-replicas=2 --replicas=3 deployment/xxx
```