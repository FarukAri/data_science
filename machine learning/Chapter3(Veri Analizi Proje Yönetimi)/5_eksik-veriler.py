# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 14:26:02 2022

@author: FARI
"""
#kutuphaneler
import pandas as pd
import numpy as np

veriler = pd.read_csv("eksikveriler.csv")

#sci-kit learn

from sklearn.impute import SimpleImputer

a = SimpleImputer(missing_values=np.nan , strategy="mean")

yas = veriler.iloc[:,1:4].values

a = a.fit(yas)
yas = a.transform(yas)
print(yas[:,1:4])

