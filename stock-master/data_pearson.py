import requests
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def pearson(path,result):
    # 讀取檔案
    df=pd.read_csv("data/"+path+".csv", encoding = 'utf-8')
    print(df.shape)

    # 印出pearson結果
    df1=df.iloc[:,2::]
    print(df1.shape)

    df1_corr=df1.corr()

    print('===============================')

    ### 去掉高度相關的欄位 ###

    # 取得上三角的值
    upper = df1_corr.where(np.triu(np.ones(df1_corr.shape), k=1).astype(np.bool))

    # 找到corr大於0.9的欄位，並刪除
    to_drop = [column for column in upper.columns if any(upper[column] > 0.9)]
    print(to_drop)
    df.drop(to_drop, axis=1, inplace=True)

    # 增加分類標籤，盈餘正為1，負為0
    if result == "基本每股盈餘（元）":
        df['label'] = df[result].map(lambda x: 1 if x > 0 else 0)
    elif result == "每股參考淨值":
        df['label'] = df[result].map(lambda x: 1 if x > 20 else 0)

    # 印出整理後的欄位
    print(df.shape)
    df.to_csv('data/'+path+'_after_pearson.csv',mode='a',encoding='utf-8-sig',index=0)
    return 'finish'

#pearson("income_sheet_clean","基本每股盈餘（元）")
pearson("balance_sheet_clean","每股參考淨值")



## 繪圖
#plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
#sns.heatmap(df1.corr(method ='pearson'),annot=True)
#sns.pairplot(df1)
#plt.show()
