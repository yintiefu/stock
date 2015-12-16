# -*- coding:utf-8 -*-
__author__ = 'ellis.yin'
import tushare as ts
from sqlalchemy import create_engine
import pandas as pd
import ilhb


# fs = ts.top_list()
# fs['dif'] = fs.apply(lambda x: float(x.buy) - float(x.sell), axis=1)
# fs.mask(lambda x: float(x.dif) > 0)
# print(fs)
# cf = fs[fs['dif'] > 0]
# grouped.filter(lambda x: x['A'].sum() + x['B'].sum() > 0)
# [x for x in fs if x['dif'] > 0]
# print (cf)
# fs.to_sql('lhb_daily', engine, if_exists='append')
# df = pd.read_sql_query("select code,reason,date from lhb_daily", engine)
# for x, y, z in df.values:
# print x, y, z

df = ts.get_hist_data('600637')
# df['code'] = '600637'
# df = df.drop(['v_ma5', 'v_ma10', 'v_ma20'], axis=1)
# df.to_sql('qt_daily_k', engine, if_exists='append')
print len('2014-12-05,13.9600,14.0500,15.2300,13.5200,14.5300,441369720,6338168164.5200,145469')
