import requests
import pandas as pd
import numpy as np

def miss0(path,encodeing):
    df=pd.read_csv("data/"+path+".csv", encoding = encodeing,error_bad_lines=False)
    print(df.shape)
    df_f=df.iloc[:,0:3]
    df_b=df.iloc[:,3::]

    # 將缺失值替換為0
    for i in df_b.columns:
        if df_b[i].dtypes == 'int64' or df_b[i].dtypes == 'float64':
            #print('a:',i,df_b[i].dtypes)
            df_b[i]=df_b[i].replace('--','0')
        else:
            #print('b:',i,df_b[i].dtypes)
            df_b[i]=df_b[i].str.replace('--','0')
    df_b = df_b.iloc[:,:].astype(float)

    df = pd.concat([df_f, df_b], axis=1, sort=False)
    print(df.shape)
    #print(df.info())
    df.to_csv("data/"+path+"_clean.csv",encoding='utf-8-sig',index=0)
    return 'finish'

#miss0("income_sheet","cp950")
miss0("balance_sheet","utf-8")
