# -*- coding:utf-8 -*-
__author__ = 'Ellis.yin'
import datetime
import ilhb
from sqlalchemy import create_engine
import pandas as pd


def init_lhb_daily():
    engine = create_engine('mysql://root:!@55e4043822731.gz.cdb.myqcloud.com:5073/stock?charset=utf8')
    for i in range(0, 300, 1):
        s = '2014-08-18'
        today = datetime.datetime.strptime(s, '%Y-%m-%d').date()
        date = today - datetime.timedelta(i)
        print date
        try:
            fs = ilhb.lhb_daily(date, pause=0.5)
        except Exception as e:
            print('%s非交易日' % str(date))
            pass
        else:
            fs.to_sql('lhb_daily', engine, if_exists='append', index=False)
            print fs

#select lbd.*,lbc.name from lhb_broker_detail lbd right join `lhb_broker_code` lbc on lbd.traderId = lbc.traderId where lbd.`date`='2015-09-24'
# union select lbd.*,lbc.name from lhb_broker_detail lbd right join `lhb_broker_code` lbc on lbd.traderId = lbc.traderId where lbd.`date`='2015-09-23'


def init_lhb_broker_detail():
    engine = create_engine('mysql://root:ytf19890416!@55e4043822731.gz.cdb.myqcloud.com:5073/stock?charset=utf8')
    res = pd.read_sql_query('select * from lhb_broker_code where cat_id=1',engine)
    for traderId in res['traderId']:
        df = ilhb.lhb_trader_detail(traderId)
        df.to_sql('lhb_broker_detail', engine, if_exists='append', index=False)
        print df

if __name__ == "__main__":
    init_lhb_broker_detail()