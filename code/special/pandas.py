import pandas as pd
import numpy as np

'''=============================================
            pandas
series:一维数据结构
dataframe:二维数据结构





================================================'''





df =pd.DataFrame(np.random.randn(6,4),columns=list('ABCD'))  #创建多维数组
print df
print df.iloc[3]                  #获取第4行
type(df.iloc[3])            #得到 Series
#切片操作
df.iloc[3:5,0:2]            #获取4~5行，1~2列的数据
df.iloc[[1,2,4],[0,2]]      #获取2，3，5行，1，2列的数据
df.iloc[1:3,:]              #获取2~3行的所有列数据
df.iloc[:,1:3]              #获取2~3列的所有行数据
df.iloc[1,1]                #获取特定位置的值，功能等同与iat
df.iat[1,1]                 #比iloc更高效

#TODO 为什么iat比iloc高效

