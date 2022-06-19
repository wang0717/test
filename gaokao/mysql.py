#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：test 
@File    ：mysql.py
@Author  ：Wang
@Date    ：2022/5/18 19:55 
@Show    :执行数据库命令
fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
fetchall(): 接收全部的返回结果行.
rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
https://www.runoob.com/python3/python3-mysql.html
"""

import pymysql


def sql(txt):
    # 打开数据库连接
    db = pymysql.connect(
        host="bj-cynosdbmysql-grp-r88934t4.sql.tencentcdb.com",
        port=23191,
        user="root",
        passwd="Wzq960929",
        database="gaokao")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 定义要执行的SQL语句

    sql = txt

    # 执行SQL语句
    cursor.execute(sql)
    # 查询单条数据
    data = cursor.fetchall()
    #print(data);
    # 关闭光标对象
    cursor.close()
    # 关闭数据库连接
    db.close()
    return data


if __name__ == '__main__':
    sql("select * from ceshi where id = 1")
