# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:56:26 2022

@author: FARI
"""

#kutuphaneler
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Veri Yükleme

veriler = pd.read_csv("maaslar.csv")


# Data Frame Dilimleme(slicing)
x = veriler.iloc[:,1:2].values
y = veriler.iloc[:,2:].values

# Linear Regression
from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(x,y)


# Polynomial Regression (2. dereceden)

from sklearn.preprocessing import PolynomialFeatures

poly_reg =PolynomialFeatures(degree = 2)
x_poly = poly_reg.fit_transform(x)

lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly, y)


# Polynomial Regression (4. dereceden)


from sklearn.preprocessing import PolynomialFeatures

poly_reg3 =PolynomialFeatures(degree = 4)
x_poly3 = poly_reg.fit_transform(x)

lin_reg3 = LinearRegression()
lin_reg3.fit(x_poly3 , y)


# Görselleştirme

plt.scatter(x,y, color="red")
plt.plot(x, lin_reg.predict(x))

plt.scatter(x,y)
plt.plot(x, lin_reg2.predict(x_poly), color="red")

plt.scatter(x,y)
plt.plot(x, lin_reg3.predict(x_poly3), color="red")

