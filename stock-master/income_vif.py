import requests
import pandas as pd
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor
import seaborn as sns
import matplotlib.pyplot as plt


def checkVIF_new(df):
    df['const']=[1 for j in range(len(df))]
    name = df.columns
    x = np.matrix(df)
    VIF_list = [variance_inflation_factor(x,i) for i in range(x.shape[1])]
    VIF = pd.DataFrame({'feature':name,"VIF":VIF_list})
    
    VIF = VIF.drop(VIF[VIF.feature=='const'].index)
    print(VIF)

    return VIF

if __name__ == "__main__":
    df=pd.read_csv("data/income_clean.csv", encoding = 'utf-8')
    df=df.iloc[:,2:5]
    print(df.info())
    print(df.describe())
    checkVIF_new(df)

    #指定字型
    #plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
    #sns.pairplot(df)
    #plt.savefig('income_vif.png')
    #plt.show()




