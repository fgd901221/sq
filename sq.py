#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: GD

import pandas as pd
import numpy as np
pd.set_option('display.width',1000)
# df = pd.read_excel('survey_user_answer_effective.xls',skiprows=[0])
df = pd.read_csv('effect.csv')
# data = pd.read_table('survey_user_answer_effective.txt',header=None,encoding='utf-8',delim_whitespace=True,index_col=0)
# print df
# print df
# print df.ix[0:10]
def clean_answer_cont(df):
    # print df
    # print type(df)
    # print str(df)
    if df == '':
        # print 11
        # print df
        return 0
    elif str(df) == 'nan':
        # print 33
        # print df
        # print str(df)
        return 0
    elif len(df) > 2:
        # print 22
        # print df
        return 0

    else:
        # print 44
        # print df
        return df
# print len(df['answer_content'].unique())
# print df['answer_content'][0]
# print len(df['answer_content'][0])
# print '========'
df['answer_content']= df['answer_content'].apply(clean_answer_cont)
# for i in df:
#     i['answer_content'] = clean_answer_cont(i['answer_content'])
group_by_question= df.groupby(['question_id']).mean()
# group_by_question= df.groupby(['question_id'],as_index=False)
# print "===="
# print df
# print group_by_question.mean()
# print group_by_question['answer_content'].mean()
# print df.ix[0:10]
print df['answer_content'][0]
print len(df['answer_content'].unique())
df_count=df['answer_content'].unique()

print group_by_question
