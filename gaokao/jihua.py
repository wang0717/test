#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：test 
@File    ：jihua.py
@Author  ：Wang
@Date    ：2022/5/18 20:26 
@Show    :
"""
from mysql import sql
from distinct import distinct
from distinct import distinct2
import xlwt  # 导入xlwt模块


# sql语句查询文理、院校、专业相同的数据
l1 = """
SELECT
	21year.*, 
	20years.*
FROM
	21year,
	20years
WHERE
	21year.`文理` = 20years.`文理` AND
	21year.`院校名称` = 20years.`院校名称` AND
	21year.`专业名称` = 20years.`专业名称`
ORDER BY
	21year.id ASC
"""
l2 = sql(l1)
# 删除重复数据，存在部分重复数据
l3 = distinct(l2)


# 获取查询出多少条数据，一条数据多少个值
lang1 = len(l3)
lang2 = len(l3[0])


# 写入Excel
# 1 新建工作簿
workbook = xlwt.Workbook()
# 2 新建工作表并重命名
worksheet = workbook.add_sheet('Python')  # 将工作表worksheet命名为‘Python’
# 3 写入内容
i = 0
for x in range(0,lang1):
    num1 = x
    num2 = l3[i][0]
    # print("x:",x,"i:",i,"值:",l2[i][0])
    if x == l3[i][0]:
        for y in range(0, lang2):
            worksheet.write(x-1, y, l3[i][y])  # write(行,列,写入的内容)
        i = i + 1
# 4 保存
workbook.save('B:\桌面\qwe.xls')
