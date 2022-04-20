# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 03:14:04 2022

@author: FARI

"""
#kutuphaneler

import pandas as pd
import numpy as np

veriler = pd.read_csv("odev_tenis.csv")

t = veriler.iloc[:,1].values


# Kategorik Verilerden Numerik Verilere Geçiş Yöntemi

from sklearn import preprocessing

# Outlook

ol = veriler.iloc[:,:1].values


le = preprocessing.LabelEncoder()
ol[:,0] = le.fit_transform(veriler.iloc[:,0].values)


ohe = preprocessing.OneHotEncoder()
ol = ohe.fit_transform(ol).toarray()


# Play

p = veriler.iloc[:,4:].values


le = preprocessing.LabelEncoder()
p[:,0] = le.fit_transform(veriler.iloc[:,4:].values)


ohe = preprocessing.OneHotEncoder()
p = ohe.fit_transform(p).toarray()


# Windy

w = veriler.iloc[:,3:4].values


le = preprocessing.LabelEncoder()
w[:,0] = le.fit_transform(veriler.iloc[:,3:4].values)


ohe = preprocessing.OneHotEncoder()
w = ohe.fit_transform(w).toarray()




# Kategorileri Birleştirme

s1 = pd.DataFrame(data=ol, index=range(14), columns=["overcast","rainy","sunny"])
s2 = pd.DataFrame(data=w[:,:1], index=range(14), columns=["Windy_False"])
s3 = pd.DataFrame(data=p[:,:1], index=range(14), columns=["Play_No"])
s4 = pd.DataFrame(data=veriler.iloc[:,2:3].values, index=range(14), columns=["Humidity"])
s5 = pd.DataFrame(data=t, index=range(14), columns=["Temperature"])


# DataFrame Birleştirme
'''
df1 = pd.concat([s1, s4, s2, s3], axis=1)


# Veri Kümesinin Eğitim ve Test Olarak Bölünmesi


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(df1, s5, test_size=0.33, random_state=0)


from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)



import statsmodels.api as sm

X = np.append( arr=np.ones((14,1)).astype(int), values=df1, axis=1)

X_list = df1.iloc[:,[0,1,2,3,4,5]].values
X_list = np.array(X_list, dtype = float)
model = sm.OLS(t, X_list).fit()

print(model.summary())

'''

# p values baz alınarak eleme yaparsak


df2 = pd.concat([s1, s4], axis=1)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(df2, s5, test_size=0.33, random_state=0)


from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred2 = regressor.predict(x_test)

import statsmodels.api as sm

X = np.append( arr=np.ones((14,1)).astype(int), values=df2, axis=1)

X_list = df2.iloc[:,[0,1,2]].values
X_list = np.array(X_list, dtype = float)
model = sm.OLS(t, X_list).fit()

print(model.summary())



