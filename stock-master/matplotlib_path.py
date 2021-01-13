# 解決圖片無法顯示中文
# 先去下載TaipeiSansTCBeta-Regular.ttf字型檔
# 到C:/user/username/.matplotlib 刪除fontList.json檔案，重新import matplotlib

#執行以下程式找路徑，並在matplotlib/mpl-data/fonts/ttf放入以下好的字型檔
import matplotlib
print(matplotlib.__file__)

#找到所有字型檔
import matplotlib.font_manager 
a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
for i in a:
    print(i)
