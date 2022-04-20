# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 14:26:02 2022

@author: FARI
"""
#kutuphaneler
import pandas as pd
import numpy as np

veriler = pd.read_csv("veriler.csv")


# Eksik veriler

# sci-kit learn

from sklearn.impute import SimpleImputer

a = SimpleImputer(missing_values=np.nan , strategy="mean")

yas = veriler.iloc[:,1:4].values


yas = a.fit_transform(yas)



# Kategorik Verilerden Numerik Verilere Geçiş Yöntemi


ulke = veriler.iloc[:,:1].values


from sklearn import preprocessing

le = preprocessing.LabelEncoder()
ulke[:,0] = le.fit_transform(veriler.iloc[:,0].values)


ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()


##### Cinsiyet


c = veriler.iloc[:,:1].values

c[:,-1] = le.fit_transform(veriler.iloc[:,-1].values)

c = ohe.fit_transform(c).toarray()

# Kategorileri Birleştirme

sonuc1 = pd.DataFrame(data=yas , index=range(22), columns=["boy","kilo","yaş"])

sonuc2 = pd.DataFrame(data=ulke, index=range(22) , columns=["fr","tr","us"])


sonuc3 = pd.DataFrame(data=c[:,:1], index=range(22), columns=["cinsiyet"])

# DataFrame birleştirme
df1 = pd.concat([sonuc2,sonuc1], axis=1)
df2 = pd.concat([df1, sonuc3], axis=1)



# Veri Kümesinin Eğitim ve Test Olarak Bölünmesi


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(df1, sonuc3, test_size=0.33, random_state=0)


from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)


boy = df2.iloc[:,3:4].values

sol = df2.iloc[:,0:3]
sag = df2.iloc[:,4:]

veri = pd.concat([sol, sag], axis=1)


x_train, x_test, y_train, y_test = train_test_split(veri, boy, test_size=0.33, random_state=0)

r2 = LinearRegression()
r2.fit(x_train, y_train)

y_pred = r2.predict(x_test)





import statsmodels.api as sm

X = np.append( arr=np.ones((22,1)).astype(int), values=veri, axis=1)

X_list = veri.iloc[:,[0,1,2,3,4,5]].values
X_list = np.array(X_list, dtype = float)
model = sm.OLS(boy, X_list).fit()

print(model.summary())


'''
# 5. sütünu atıyoruz

X_list = veri.iloc[:,[0,1,2,3,5]].values
X_list = np.array(X_list, dtype = float)
model = sm.OLS(boy, X_list).fit()

print(model.summary())

'''



