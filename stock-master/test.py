import requests
from io import StringIO
import pandas as pd
import numpy as np
import datetime
import time
import stock_id

def crawl_three(date):
    r = requests.get('https://www.twse.com.tw/fund/T86?response=csv&date=' + str(date).split(' ')[0].replace('-','') + '&selectType=ALL')
    try:
        df = pd.read_csv(StringIO(r.text),header=1)
    
        # 指定ID篩選
        new_df=df[df['證券代號'].isin(stock_id.id())]  
        
        # 插入時間欄位，並將欄位移至最前面
        new_df['time']=date
        cols = new_df.columns.tolist()
        cols = cols[-1:] + cols[:-1]
        new_df=new_df[cols]

        print('當日交易ID筆數',len(new_df))
        new_df.to_csv('stock_three_test.csv',mode='a',encoding='utf-8-sig', index=0,header=0)
        
        return new_df

    except Exception as e:
        print('what happend:',e)


data = {}
n_days = 20
# date = datetime.datetime.now()
date0 = '2020-02-01 09:01:01.403545'
date = datetime.datetime.strptime(date0,'%Y-%m-%d %H:%M:%S.%f')

fail_count = 0
allow_continuous_fail_count = 5

new_df=pd.DataFrame(columns=['time','證券代號','證券名稱','外陸資買進股數(不含外資自營商)','外陸資賣出股數(不含外資自營商)','外陸資買賣超股數(不含外資自營商)',
'外資自營商買進股數','外資自營商賣出股數','外資自營商買賣超股數','投信買進股數','投信賣出股數','投信買賣超股數','自營商買賣超股數','自營商買進股數(自行買賣)','自營商賣出股數(自行買賣)',
'自營商買賣超股數(自行買賣)','自營商買進股數(避險)','自營商賣出股數(避險)','自營商買賣超股數(避險)','三大法人買賣超股數'])
new_df.to_csv('stock_three_test.csv',encoding='utf-8-sig',index=0)
while len(data) < n_days:

    print('parsing', date)
    # 使用 crawPrice 爬資料
    try:
        # 抓資料
        data[date.date()] = crawl_three(date)
        print('==================success!=====================')
        fail_count = 0
        
    except:
        # 假日爬不到
        print('========fail! check the date is holiday========')
        fail_count += 1
        if fail_count == allow_continuous_fail_count:
            raise
            break
    
    # 減一天
    date -= datetime.timedelta(days=1)
    time.sleep(5)