## 查看conda版本
conda -version
conda -V

## 查看包含版本更多信息
conda info

## 更新conda
conda update conda

## 查看conda环境管理命令帮助信息
conda create -help

## 新建虚拟环境
conda create -name <env_name>

## 删除虚拟环境
conda remove -name <env_name> --all

## 创建指定Python版本，指定包
conda create -n <env_name> python=3.7
conda create -n <env_name> scipy
conda create -n <env_name> scipy=0.15.0
conda create -n <env_name> python=3.7 scipy=0.15.0 numpy request

## 给虚拟环境安装包
conda install scipy
conda install scipy=0.15.0
conda install scipy curl
conda install scipy=0.15.0 curl=7.26.0

conda install -n <env_name> scipy
conda install -n <env_name> scipy=0.15.0

## 查看当前环境的包
conda list

## 更新包
conda update
conda update numpy
conda update conda
conda update anaconda

## 删除包
conda remove numpy
conda remove numpy pandas
conda remove -n <env_name> numpy pandas

## 搜索包
conda search numpy

## 克隆一个环境
conda create --name <clone_name> --clone <env_name>

1.获取版本号
    conda -V
    conda --version

2.查看所以虚拟环境
    conda env list
    conda info -e

3.进入某个虚拟环境（激活）
    conda activate env_name（虚拟环境名）

4.退出当前虚拟环境
   conda deactivate [env_name（虚拟环境名）]  

5.创建新的虚拟环境
    conda create -n env_name（虚拟环境名）python=3.7.3（python的版本号）[anaconda]
    conda create --name env_name（虚拟环境名）python=3.7.3（python的版本号）[anaconda]

6.删除虚拟环境
    conda remove -n env_name（虚拟环境名）--all

7.复制环境
    conda create -n new_env_name（新的虚拟环境名）--clone env_name（虚拟环境名） 

8.列举当前虚拟环境下所有的包
    conda list  

9.指定安装包版本
    conda install package_name=2.1（包名的版本号）

10.移除环境中的包
    conda remove -n env_name（虚拟环境名）package_name（包名）
    conda remove --name env_name（虚拟环境名）package_name（包名）

10.查看包的依赖
    conda info pack_name（包名）

11.更新当前conda版本和anaconda版本
    conda update conda 
    conda update anaconda

12.查看conda的命令使用
    conda -h
    conda --help

13.更新包
    conda update package_name（包名）

14.阻止conda自己更新
    conda config --set auto_update_conda False

15.anaconda换源
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
查询完整帮助文件
conda create --help or conda create -h 其实“--”参数一般都有简写。

管理conda和anaconda
conda info 查询conda信息
conda update conda 升级conda
conda update anaconda 升级anaconda

管理环境
conda info -e 环境信息
conda create -n test python=2.7 创建环境test，并指定python版本，此例为2.7
source activate test 激活环境
source deactivate test 关闭环境
conda remove --name test --all 删除环境

包管理
conda list 列出所有安装的包的信息
conda search beautiful-soup 查询包
conda install -n test beautiful-soup 安装包，并指定安装环境，如果没有-n test，则安装到当前环境
conda update beautiful-soup 升级包
conda remove -n test beautiful-soup 移除包

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple <package_name>