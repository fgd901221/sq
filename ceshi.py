#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: GD

import pandas as pd
import numpy as np
pd.set_option('display.width',1000)
# df = pd.read_excel('survey_user_answer_effective.xls',skiprows=[0])
df = pd.read_csv('effect.csv')

str1 = df['answer_content'][3]
str2='nan'
print str1
print type(str1)
print str(str1)
print float(str2)

fgd =np.array([1.0,float(str2),str1])
print fgd
print '====='
print fgd.min()