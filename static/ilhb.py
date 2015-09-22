# -*- coding:utf-8 -*-
__author__ = 'Ellis.yin'

import _PyV8 as pyv8
import json
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request
import pandas as pd
import tushare as ts
from tushare.util import dateu as du
from sqlalchemy import create_engine

LHB_SINA_URL = 'http://vip.stock.finance.sina.com.cn/q/api/jsonp.php/var%%20details=/InvestConsultService.getLHBComBSData?symbol=%s&tradedate=%s&type=%s'
LHB_SINA_COLUMNS = ['code', 'buyAmount', 'sellAmount', 'netAmount', 'brokerCode', 'brokerName', 'type']

# 东方财富
LHB_EASTMONEY_URL = 'http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=LHB&sty=YYTJ&stat=1&sr=0&st=1&p=1&ps=5000&js=var%20bROHHxBi={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22}&rt=48097157'
LHB_TRADER_CODE = ['traderId','location','name']

def lhb_trader_statistic():
    request = Request(LHB_EASTMONEY_URL)
    text = urlopen(request, timeout=10).read()
    text = text.decode('utf8')
    ctxt = pyv8.JSContext()
    ctxt.enter()
    index = text.find('{')
    text = text[index:]
    result = []
    temp = json.loads(text)
    for x in temp['data']:
        data = []
        arr = x.split(',')
        data.append(arr[0])
        data.append(arr[6])
        data.append(arr[12])
        result.append(data)
    df = pd.DataFrame(result, columns=LHB_TRADER_CODE)
    return df

def lhb_daily_detail(code, date, type):
    """
    获取个股龙虎榜买5和卖5
    :param code: 股票代码
    :param date: 日期 yyyy-MM-dd
    :param type: SINA龙虎榜类型
    :return:
    """
    if (date is None):
        date = du.today()
    request = Request(LHB_SINA_URL % (code, date, type))
    text = urlopen(request, timeout=10).read()
    text = text.decode('GBK')
    text = text.splitlines()[1]
    ctxt = pyv8.JSContext()
    ctxt.enter()
    index = text.find('{') - 1
    text = text[index:-1]
    temp = ctxt.eval(text)
    data = []
    date_columns = ['SYMBOL', 'buyAmount', 'sellAmount', 'netAmount', 'comCode', 'comName']
    for a in temp.buy:
        tempdata = []
        for k in date_columns:
            tempdata.append(a[k])
        tempdata.append('b')
        data.append(tempdata)
    for a in temp.sell:
        tempdata = []
        for k in date_columns:
            tempdata.append(a[k])
        tempdata.append('s')
        data.append(tempdata)
    df = pd.DataFrame(data, columns=LHB_SINA_COLUMNS)
    df['date'] = date
    return df


def lhb_broker():
    fs = ts.broker_tops()
    return fs


def lhb_daily(date, pause=0.5):
    """
    每日龙虎榜数据
    :param date:
    :return:
    """
    fs = ts.top_list(date, pause=pause)
    fs['dif'] = fs.apply(lambda x: float(x.buy) - float(x.sell), axis=1)
    return fs


if __name__ == "__main__":
    lhb_trader_statistic()
    # df = lhb_daily('2015-09-18')
    # df = ts.inst_detail()
    # df = lhb_daily_detail('000977', '2015-09-11', '01')
    # df['type'] = 1
    # data = np.random.rand(6,4)
    # clos = ['code','name','type','index','date','broker','bamount','samount']
    # engine = create_engine('mysql://root:ytf19890416!@55e4043822731.gz.cdb.myqcloud.com:5073/stock?charset=utf8')
    # df.to_sql('lhb_broker_code', engine, if_exists='append')
    # date = datetime.datetime.strptime('2015-09-13', '%Y-%m-%d');
    # date = datetime.datetime.strptime(str(date), '%Y%m%d')
    # date = date.strftime('%Y%m%d')
    # print(df)
