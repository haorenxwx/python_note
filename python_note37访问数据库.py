python_note37访问数据库.py

基于表 table 的一对多的关系就是关系数据库的基础

直接通过python接口调用：
1：操作关系数据库，需要连接到数据库--Connection

2：连接后，需要打开游标Cursor，通过Cursor执行SQL语句
# 导入SQLite驱动:
>>> import sqlite3#直接内置在python的标准库中，所以可以直接操作
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
>>> conn = sqlite3.connect('test.db')
# 创建一个Cursor:
>>> cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
>>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
<sqlite3.Cursor object at 0x10f8aa260>
# 继续执行一条SQL语句，插入一条记录:
>>> cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
<sqlite3.Cursor object at 0x10f8aa260>
# 通过rowcount获得插入的行数:
>>> cursor.rowcount
1
# 关闭Cursor:
>>> cursor.close()
# 提交事务:
>>> conn.commit()
# 关闭Connection:
>>> conn.close()

查询记录：
>>> conn = sqlite3.connect('test.db')
>>> cursor = conn.cursor()
# 执行查询语句:
>>> cursor.execute('select * from user where id=?', ('1',))# ？表示从后面传入特定参数
<sqlite3.Cursor object at 0x10f8aa340>
# 获得查询结果集:
>>> values = cursor.fetchall()
>>> values
[('1', 'Michael')]
>>> cursor.close()
>>> conn.close()



MySQL:
安装：https://www.jianshu.com/p/fd3aae701db9
设置环境变量 https://www.jianshu.com/p/acb1f062a925
initial password: <Ktqm9yLsMDb


