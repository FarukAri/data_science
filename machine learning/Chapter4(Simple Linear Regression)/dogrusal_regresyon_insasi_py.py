# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 18:50:13 2020

@author: sadievrenseker
"""

#1.kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2.veri onisleme
#2.1.veri yukleme
veriler = pd.read_csv('satislar.csv')

#pd.read_csv("veriler.csv")
#test



aylar = veriler[["Aylar"]] #bağımsız değişkenler
satislar = veriler[["Satislar"]] #bağımlı değişken



#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split

aylar_train, aylar_test,satislar_train,satislar_test = train_test_split(aylar,satislar,test_size=0.33, random_state=0)

'''
#verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

aylar_train_sc = sc.fit_transform(aylar_train)
aylar_test_sc = sc.fit_transform(aylar_test)

satislar_train_sc = sc.fit_transform(satislar_train)
satislar_test_sc = sc.fit_transform(satislar_test)

'''
# Model İnşası (Linear Regression)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(aylar_train,satislar_train)


satislar_pred = lr.predict(aylar_test)

aylar_train = aylar_train.sort_index()
satislar_train = satislar_train.sort_index()


plt.plot(aylar_train, satislar_train)
plt.plot(aylar_test, satislar_pred)

plt.title("Aylara Göre Satış Değerleri")
plt.xlabel("Aylar")
plt.ylabel("Satış Miktarları")








