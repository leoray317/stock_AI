import requests
import numpy as np
import pandas as pd

# 取得上市股市相關資訊的csv檔。並使用.tolist()轉其id轉成list

def id():
    data=pd.read_csv('data/stock_info.csv')
    x=data['證券代號'].tolist()
    return x
