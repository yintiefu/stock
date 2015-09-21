# -*- coding:utf-8 -*-
__author__ = 'Ellis.yin'
import datetime
import ilhb
from sqlalchemy import create_engine
import pandas as pd


def init_lib_daily():
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
            fs.to_sql('lhb_daily', engine, if_exists='append')
            print fs


if __name__ == "__main__":
    init_lib_daily()