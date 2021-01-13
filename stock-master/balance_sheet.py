import requests
import pandas as pd
import numpy as np

# 資產負債表
def tot(year,season):

    # 爬蟲請求
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }
    url = 'https://mops.twse.com.tw/mops/web/t163sb05'
    data={
            'encodeURIComponent':1,
            'step':1,
            'firstin':1,
            'off':1,
            'TYPEK':'sii',
            'year':year,
            'season':season,
        }
    r = requests.post(url, data=data, headers=headers)
    r.encoding = 'utf8'
    df=pd.read_html(r.text)[12]

    # 判斷是否有多餘欄位
    for col in df.columns.values.tolist():
        if col not in columns[1:] and col == '待註銷股本股數（單位：股）':
            print('無此欄位:',col)
            df=df.drop(col,axis=1)
       


    # 新增日期並調整欄位位置
    df['date']=str(year)+str(season)
    cols = df.columns.values.tolist()
    cols = cols[-1:] + cols[:-1]
    df=df[cols]

    # 存入CSV
    df.to_csv('data/balance_sheet.csv',mode='a',encoding='utf-8-sig', index=0, header=0)

    return print('筆數:',len(df['date']))


# 建立欄位名稱並存入CSV
columns=['date','公司代號', '公司名稱', '流動資產', '非流動資產', '資產總額', '流動負債', '非流動負債', '負債總額', '股本', '資本公積', '保留盈餘', '其他權益', '庫藏股票', '歸屬於母公司業主之權益合計', '共同控制下前手權益',
 '合併前非屬共同控制股權', '非控制權益', '權益總額', '預收股款（權益項下）之約當發行股數（單位：股）', '母公司暨子公司所持有之母公司庫藏股股數（單位：股）', '每股參考淨值']

df=pd.DataFrame(columns=columns)
df.to_csv('data/balance_sheet.csv',encoding='utf-8-sig',index=0)

# 控制爬取年度與季
for year in range(102,110):
    for season in [1,2,3,4]:
        try:
            print(year,season)
            tot(year,season)
        except Exception as e:
            print('what:',e)

