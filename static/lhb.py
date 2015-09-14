# -*- coding:utf-8 -*-
__author__ = 'Ellis.yin'

import _PyV8 as pyv8

try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request
import pandas as pd
from tushare.util import dateu as du

LHB_SINA_URL = 'http://vip.stock.finance.sina.com.cn/q/api/jsonp.php/var%%20details=/InvestConsultService.getLHBComBSData?symbol=%s&tradedate=%s&type=%s'
LHB_SINA_COLUMNS = ['code', 'buyAmount', 'sellAmount', 'netAmount', 'brokerCode', 'brokerName', 'type']


def get_data(code, date, type):
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
    print(text)
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


if __name__ == "__main__":
    df = get_data('000977', '2015-09-11', '01')
    # data = np.random.rand(6,4)
    # clos = ['code','name','type','index','date','broker','bamount','samount']
    # engine = create_engine('mysql+mysqlconnector://root:ytf19890416!@55e4043822731.gz.cdb.myqcloud.com:5073/stock?charset=utf8')
    # df.to_sql('lhb_daily_broker',engine,if_exists='append')
    # date = datetime.datetime.strptime('2015-09-13', '%Y-%m-%d');
    # date = datetime.datetime.strptime(str(date), '%Y%m%d')
    # date = date.strftime('%Y%m%d')
    # print(df)
