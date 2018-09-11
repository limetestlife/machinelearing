# -*- coding: UTF-8 -*-
#Step 1: 导库 numpy,pandas
import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer
#Step 2: 导入数据
rootpath = os.path.abspath('..')  # 获取上级路径
dataset=pd.read_csv(rootpath+'\date\Data.csv')
print dataset

X = dataset.iloc[ : , :-1].values
Y = dataset.iloc[ : , 3].values

#TODO .values的作用

print X
print Y

#处理缺失值
imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
imputer = imputer.fit(X[ : , 1:3])
X[ : , 1:3] = imputer.transform(X[ : , 1:3])
print X
