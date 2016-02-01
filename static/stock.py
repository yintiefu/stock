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
zxb = ts.get_sme_classified()
engine = create_engine('mysql://root:password!@55e4043822731.gz.cdb.myqcloud.com:5073/stock?charset=utf8')
sql = "INSERT INTO five_minute_data(code,date,t_3_00,t_2_55,t_2_50,t_2_45,t_2_40,t_2_35) VALUES('%s','%s','%s','%s','%s','%s','%s','%s')"
for code in zxb['code']:
    connection = engine.connect()
    df = ts.get_hist_data(code, start='2016-01-29', end='2016-01-30', ktype='5')
    # df['code'] = '600637'
    df = df.drop(
        ['ma5', 'ma10', 'ma20', 'v_ma5', 'v_ma10', 'v_ma20', 'open', 'close', 'low', 'high', 'volume', 'price_change',
         'turnover'], axis=1)
    # df.to_sql('five_min_data', engine, if_exists='append')
    if (df.size > 0):
        date = str(df.index[0])[0:10]
        t_3_00 = df['p_change'][0]
        t_2_55 = df['p_change'][1]
        t_2_50 = df['p_change'][2]
        t_2_45 = df['p_change'][3]
        t_2_40 = df['p_change'][4]
        t_2_35 = df['p_change'][5]
        # sql % (code, date, t_3_00, t_2_55, t_2_50, t_2_45, t_2_40, t_2_35)
        connection.execute(sql % (code, date, t_3_00, t_2_55, t_2_50, t_2_45, t_2_40, t_2_35))
    connection.close()