https://docs.helm.sh/

https://github.com/helm/helm

https://whmzsu.github.io/helm-doc-zh-cn/chart_template_guide/getting_started-zh_cn.html

查看版本
```
helm version
```

增加repo
```
helm repo add stable https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts
helm repo add --username admin --password password myharbor https://harbor.qing.cn/chartrepo/charts
```

更新repo仓库资源
```
helm repo update
```

查看当前安装的charts
```
helm list
```

将helm search hub显示所有可用图表
```
helm search hub redis
```

使用helm search repo，您可以在已添加的存储库中找到charts的名称
```
helm search repo redis
```

打印出指定的Charts的详细信息
```
helm show chart stable/redis
```

下载charts到本地
```
helm fetch redis
```

安装charts
```
helm install redis stable/redis
```

查看charts状态
```
helm status redis
```

删除charts
```
helm uninstall redis
```

创建charts
```
helm create helm_charts
```

检查chart语法正确性
```
helm lint myapp
```

打包自定义的chart
```
helm package myapp
```

查看生成的yaml文件
```
helm template myapp-1.tgz
```

使用默认chart部署到k8s
```
helm install myapp myapp-1.tgz
```

使用包去做release部署
```
helm install --name example2 helm-chart-0.1.0.tgz --set service.type=NodePort
```

更新images
```
helm upgrade myapp myapp-2.tgz
```

查看版本信息
```
helm history myapp
```

回滚指定版本
```
helm rollback myapp 1
```


```

```