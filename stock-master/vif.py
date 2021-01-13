#%%
import requests
import pandas as pd
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor
import seaborn as sns
import matplotlib.pyplot as plt

# %%
# VIF
df=pd.DataFrame({
        'a':[1.2,2.1,3,3.9,5.2,6.1],
        'b':[6,5,4,3,2,1],
        'c':[11,53,29,64,12,1],
        'd':[32.2,34.1,36.05,38.3,40.1,42.2],
        'e':[73.1,75.3,77.1,79.2,80.8,83.1]
    })

df['f']=[1 for j in range(len(df))]
name = df.columns
x = np.matrix(df)
VIF_list = [variance_inflation_factor(x,i) for i in range(x.shape[1])]
VIF = pd.DataFrame({'feature':name,"VIF":VIF_list})
VIF = VIF.drop(VIF[VIF.feature=='f'].index)

print(VIF)
print(df.describe())
sns.pairplot(df)
plt.savefig('test_vif.png')
plt.show()

# %%
# Pearson

df=pd.DataFrame({
        'a':[1.2,2.1,3,3.9,5.2,6.1],
        'b':[6,5,4,3,2,1],
        'c':[11,53,29,64,12,1],
        'd':[32.2,34.1,36.05,38.3,40.1,42.2],
        'e':[73.1,75.3,77.1,79.2,80.8,83.1]
    })
    
print(df.corr())
sns.heatmap(df.corr(),annot=True)
sns.pairplot(df)
plt.show()