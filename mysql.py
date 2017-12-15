#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: GD

import pymysql
import pandas as pd

con = pymysql.connect(host="183.134.77.144",port=4460,user="guest",password="Guest@123",db="test")
data_sql=pd.read_sql("select * from survey_user_answer_effective",con)
# print type(data_sql)
print data_sql

data_sql.to_csv("effect.csv")
