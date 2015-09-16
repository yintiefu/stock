# -*- coding:utf-8 -*-
__author__ = 'ellis.yin'
import tushare as ts
from sqlalchemy import create_engine
import pandas as pd
import ilhb


fs = ts.top_list()
fs['dif'] = fs.apply(lambda x: float(x.buy) - float(x.sell), axis=1)
# fs.mask(lambda x: float(x.dif) > 0)
# print(fs)
cf = fs[fs['dif'] > 0]
# grouped.filter(lambda x: x['A'].sum() + x['B'].sum() > 0)
# [x for x in fs if x['dif'] > 0]
print (cf)
# engine = create_engine('mysql://root:ytf19890416!@55e4043822731.gz.cdb.myqcloud.com:5073/stock?charset=utf8')
# fs.to_sql('lhb_daily', engine, if_exists='append')
# df = pd.read_sql_query("select code,reason,date from lhb_daily", engine)
# for x, y, z in df.values:
# print x, y, z

