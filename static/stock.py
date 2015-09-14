__author__ = 'ellis.yin'
import tushare as ts
from sqlalchemy import create_engine
import pandas as pd

# fs = ts.top_list()
# fs.to_excel('d:\Userdata\ellis.yin\Desktop\lhb.xls',encoding='utf-8')
engine = create_engine('mysql+mysqlconnector://root:ytf19890416!@55e4043822731.gz.cdb.myqcloud.com:5073/stock?charset=utf8')
# fs.to_sql('lhb_daily',engine,if_exists='append')
df = pd.read_sql_query("select code,reason,date from lhb_daily",engine)
for x,y,z in df.values:
    print x,y,z
print(df.T)


