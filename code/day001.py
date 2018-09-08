# -*- coding: UTF-8 -*-
#Step 1: 导库 numpy,pandas
import numpy as np
import pandas as pd

#Step 2: Importing dataset
dataset=pd.read_csv('D:\PyWork\machinelearing\date\Data.csv')
print dataset

X = dataset.iloc[ : , :-1].values
Y = dataset.iloc[ : , 3].values

