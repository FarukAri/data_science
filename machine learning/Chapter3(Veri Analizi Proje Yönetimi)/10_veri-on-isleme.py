# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 14:26:02 2022

@author: FARI
"""
#kutuphaneler
import pandas as pd
import numpy as np

veriler = pd.read_csv("eksikveriler.csv")


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


# Kategorileri Birleştirme

sonuc1 = pd.DataFrame(data=yas , index=range(22), columns=["boy","kilo","yaş"])

sonuc2 = pd.DataFrame(data=ulke, index=range(22) , columns=["fr","tr","us"])


cinsiyet = veriler.iloc[:,-1].values

sonuc3 = pd.DataFrame(data=cinsiyet, index=range(22), columns=["cinsiyet"])

# DataFrame birleştirme
df1 = pd.concat([sonuc2,sonuc1], axis=1)
df2 = pd.concat([df1, sonuc3], axis=1)



# Veri Kümesinin Eğitim ve Test Olarak Bölünmesi


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(df1, sonuc3, test_size=0.33, random_state=0)



# Öznitelik Ölçekleme (Farklı kategorilerdeki birbirinden sayıca uzak sayısal değerleri birbirine benzetme işlemi)


from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

x_train_sc = sc.fit_transform(x_train)






