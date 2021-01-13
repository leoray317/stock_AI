import requests
import pandas as pd
import numpy as np

# 綜合損益表
def tot(year,season):

    # 爬蟲請求
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }
    url = 'https://mops.twse.com.tw/mops/web/t163sb04'
    data={
            'encodeURIComponent':1,
            'step':1,
            'firstin':1,
            'off':1,
            'TYPEK':'sii',
            'year':year,
            'season':season,
        }
    r = requests.post(url, data=data, headers=headers )
    r.encoding = 'utf8'
    df=pd.read_html(r.text)[12]

    # 判斷是否有多餘欄位
    for col in df.columns.values.tolist():
        if col not in columns[1:]:
            print('無此欄位:',col)
            df=df.drop(col,axis=1)
    
    # 新增日期並調整欄位位置
    df['date']=str(year)+str(season)
    cols = df.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df=df[cols]

    # 存入CSV
    df.to_csv('data/income_sheet.csv',mode='a',encoding='utf-8-sig', index=0, header=0)
    
    return print('筆數:',len(df['date']))


# 建立欄位名稱並存入CSV
columns=['date','公司代號','公司名稱','營業收入','營業成本','營業毛利（毛損）','未實現銷貨（損）益','已實現銷貨（損）益','營業毛利（毛損）淨額','營業費用',
'其他收益及費損淨額','營業利益（損失）','營業外收入及支出','稅前淨利（淨損）','所得稅費用（利益）','繼續營業單位本期淨利（淨損）','停業單位損益','合併前非屬共同控制股權損益',
'本期淨利（淨損）','其他綜合損益（淨額）','合併前非屬共同控制股權綜合損益淨額','本期綜合損益總額',
'淨利（淨損）歸屬於母公司業主','淨利（淨損）歸屬於共同控制下前手權益','淨利（淨損）歸屬於非控制權益','綜合損益總額歸屬於母公司業主','綜合損益總額歸屬於共同控制下前手權益',
'綜合損益總額歸屬於非控制權益','基本每股盈餘（元）']

df=pd.DataFrame(columns=columns)
df.to_csv('data/income_sheet.csv',encoding='utf-8-sig',index=0)


# 控制爬取年度與季
for year in range(102,110):
    for season in [1,2,3,4]:
        try:
            print(year,season)
            tot(year,season)
        except Exception as e:
            print('what:',e)
