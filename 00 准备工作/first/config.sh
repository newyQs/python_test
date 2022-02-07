#!bin/bash

# 安装vim
yum -y install vim

# 安装网络工具
yum -y install net-tools

# 安装git
yum -y install git

# 安装python3并更新pip版本
yum -y install python
pip3 install --upgrade pip

# 如果没有这个目录
cd ~
mkdir .pip && cd .pip
vim .pip.conf
# 添加
[list]
format == columns

# 安装docker
yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager --add-repo http://download.docker.com/linux/centos/docker-ce.repo
yum -y install docker-ce-18.03.1.ce
systemctl start docker
systemctl enable docker

# 安装docker-compose
# https://docs.docker.com/compose/install/
# 1. 官网安装：
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
# 2. pip安装
pip install docker-compose

# 安装samba并配置samba
yum install -y samba
systemctl stop firewalld.service
systemctl disable firewalld.service