"""
nodename    选取此节点的所有节点
/           从当前节点，选取直接子节点
//          从当前节点，选取子孙节点
.           选取当前节点
..          选取当前节点的父节点
@           选取属性

查看教程：
https://www.w3school.com.cn/xpath/index.asp
"""
from lxml import etree

"""
Xpath语法：

7种类型的节点：
元素
属性
文本
命名空间
处理指令
注释
文档节点（根节点）

"""