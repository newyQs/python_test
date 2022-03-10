# 7 MYSQL基础

## 7.1 运算符

### 7.1.1 算术运算符
```text
+ 加法
- 减法
* 乘法
/ 除法
% 求余
DIV 除法，相当于/
MOD 求余，相当于%
```


### 7.1.2 比较运算符

```text
>
<
>=
<=
=
!=或<>
IS NULL
IS NOT NULL
BETWEEN AND
IN
NOT IN
LIKE
NOT LIKE
REGEXP
```


### 7.1.3 逻辑运算符
```text
&&或AND
||或OR
!或NOT
XOR
```


### 7.1.4 位运算符
```text
&
|
~
^
<<
>>
```


### 7.1.5 运算符的优先级
```text
高
!
~
^
*, /, DIV, %, MOD
+, -
>>, <<
&
|
=, <=>, <, <=, >, >=, !=, <>, IN, IS, NULL, LIKE, REGEXP
BETWEEN AND, CASE, WHEN, THEN, ELSE
NOT
&&, AND
||, OR, XOR
:=
低

以上优先级由上而下依次递减，如果优先级相同，则表达式左边的运算符先计算。
```

## 7.2 流程控制语句


### 7.2.1 IF语句
```sql
IF <条件> THEN
...
ELSE <条件> THEN
...
ELSE
... 
ENDIF

```

### 7.2.2 CASE语句
```sql
CASE [VALUE ]
    WHEN <value> THEN ...
    [WHEN <value> THEN ...]
    [ELSE ...]
END CASE
```

### 7.2.3 WHILE语句
```sql
WHILE <条件> DO
...
END WHILE
```

### 7.2.4 LOOP语句


### 7.2.5 REPEAT语句