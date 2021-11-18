# Sf-Artifacts
## 初始化
使用 python 版本: py3.6+

使用开发数据库: postgres(可使用 docker)
### 依赖服务搭建
使用docker-compose搭建数据库等依赖，可以参考`docker/docker-compose.yml`
### 环境配置及依赖安装
```sh
python -m venv .env
source .env/bin/activate
make install
```
### 开发本地配置
创建config/local.yml文件并根据需要重写数据库等配置，示例：
```yaml
app:
  DATABASE_URI: postgresext+pool://root:sangfor@localhost:5432/artifacts
  server_url: http://localhost:7000
  ADMIN_GLOBAL_ACCESS_SWITCH: true
  Nexus:
    host: http://localhost:8081/
    username: admin
    password: admin
```

### 初始化数据库并导入seed
```
make init
make dbseed
```

## 常用命令
### 日常开发命令
```sh
# 启动服务
make dev
# 启动flask shell
make shell
# 代码语法检查
make lint
```
### 迁移相关命令
```sh
# 若修改了数据库模型字段, 需添加迁移文件
# 创建完迁移文件会在 db/migrations 里新增一个 模板, 需自行编写改动
python command.py create-migration --name {migration-name}
# 执行迁移
make migrate
# 迁移回滚
python command.py rollback --name {migration-name}
```
### 单元测试
```sh
# 跑所有用例
make test
# 仅跑携带api标签的用例
make test test_label=api
```
### 更多命令
请参照`Makefile`以及`lib.commands`

## 提交规范

规范格式: `type(scope): msg`

**type** 提交类型:  
refact: 不影响使用的修改, 对某些代码进行重构  
fix: 修复某个问题  
feat: 添加某个功能  
build: 构建相关  
doc: 文档相关  

**scope** 修改范围, 可不写:  
具体相关业务的范围, 可理解为模块, egs: product, version, module  

**msg**:  
一句话写提交信息, 若需要详细描述则空一行再写  

```
feat(product): 添加产品xxx功能

具体这个功能的描述 xxxxx
```

## 开发注意事项
- 编码实现功能后需要执行`make lint`, `make test`清除坏味道保证用例仍然有效
- 如果添加了系统依赖需要修改docker/Dockerfile.env.base并执行`make build-env-base`，手动构建envbase镜像并推上docker源
- 如果修改了requirements.txt，需要执行`make build-base`，手动构建base镜像并推上docker源

## 部署注意
- 正式部署时需要手动执行make dbseed操作插入数据
- 需要为docker-registry手动创建eds bucket
- 正式环境的数据库等参数需要以local.yml的形式写入线上环境，禁止将线上环境的账号密码等敏感数据提交上库