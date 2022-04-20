# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 18:56:53 2022

@author: FARI
"""

#1.kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score
import statsmodels.api as sm

veriler = pd.read_csv("maaslar_yeni.csv")


x = veriler.iloc[:,2:5].values
y = veriler.iloc[:,5:].values


#multiple linear regression
from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(x, y)

y_pred = lin_reg.predict(x)

#MLR için p value

model = sm.OLS(lin_reg.predict(x), x)
print(" ")
print("*****************************MLR OLS*****************************")
print(model.fit().summary())

#polynomial regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
x_poly = poly_reg.fit_transform(x)

lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)

y_pred = lin_reg2.predict(x_poly)

#PR için p value
model2 = sm.OLS(lin_reg2.predict(poly_reg.fit_transform(x)), x)
print(" ")
print("*****************************PR OLS*****************************")
print(model2.fit().summary())

#verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler

sc1=StandardScaler()

x_olcekli = sc1.fit_transform(x)

sc2=StandardScaler()
y_olcekli = np.ravel(sc2.fit_transform(y.reshape(-1,1)))

#Support Vector Regression
from sklearn.svm import SVR

svr_reg = SVR(kernel='rbf')
svr_reg.fit(x_olcekli,y_olcekli)

#SVR için p value
model3 = sm.OLS(svr_reg.predict(x_olcekli), x_olcekli)
print(" ")
print("*****************************SVR OLS*****************************")
print(model3.fit().summary())


#Decision Tree Regresyon
from sklearn.tree import DecisionTreeRegressor
r_dt = DecisionTreeRegressor(random_state=0)
r_dt.fit(x,y)


#DTR için p value
model4 = sm.OLS(r_dt.predict(x), x)
print(" ")
print("*****************************DTR OLS*****************************")
print(model4.fit().summary())

#Random Forest Regresyonu
from sklearn.ensemble import RandomForestRegressor
rf_reg=RandomForestRegressor(n_estimators = 10,random_state=0)
a = y.ravel()
rf_reg.fit(x,y.ravel())

#RFR için p value
model5 = sm.OLS(rf_reg.predict(x), x)
print(" ")
print(" ***************************** RFR OLS ***************************** ")
print(model5.fit().summary())

#Değerlerin birbiri arasındaki ilişkiyi gösterir
print(veriler.corr())       

#Predictions