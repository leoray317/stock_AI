#%%
import requests
import pandas as pd
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor
import seaborn as sns
import matplotlib.pyplot as plt
#%%
data=pd.read_csv("data/balance_sheet.csv", encoding = 'cp950')
print(data.info())
# %%
