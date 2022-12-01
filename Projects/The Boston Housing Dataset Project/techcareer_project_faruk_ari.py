
# **KÜTÜPHANELERİN EKLENMESİ**

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

"""**KOLON İSİMLERİ**

*   CRIM - per capita crime rate by town
*   ZN - proportion of residential land zoned for lots over 25,000 sq.ft.
*   INDUS - proportion of non-retail business acres per town.
*   CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)
*   NOX - nitric oxides concentration (parts per 10 million)
*   RM - average number of rooms per dwelling
*   AGE - proportion of owner-occupied units built prior to 1940
*   DIS - weighted distances to five Boston employment centres
*   RAD - index of accessibility to radial highways
*   TAX - full-value property-tax rate per 10,000  dollar
*   PTRATIO - pupil-teacher ratio by town
*   B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
*   LSTAT - % lower status of the population
*   MEDV - Median value of owner-occupied homes in $1000's
"""

column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# VERİLERİN YÜKLENMESİ

housing = pd.read_csv("housing.csv", header=None, delimiter=r"\s+", names=column_names)

# VERİYİ TANIMA İŞLEMLERİ

print(np.shape(housing))
print("************************************************************************")
print(housing.items())
print("************************************************************************")
print(housing.head(10))
print("************************************************************************")
print(housing.describe())
print("************************************************************************")
print(housing.isnull().sum())
print("************************************************************************")

# VERİDEKİ KOLONLAR ARASINDAKİ İLİŞKİYİ GÖRMEK İÇİN HEATMAP OLUŞTURMA

sns.set(rc = {'figure.figsize':(15,8)})
correlation_matrix = housing.corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True)

del housing["CHAS"]
print(housing)
print("************************************************************************")

# HER KOLONDAKİ OUTLIERS DEĞERLERİ YÜZDELİK İLE ÖLÇME

print(" KOLONLARDAKİ OUTLIERS DEĞERLERİ ")

for k, v in housing.items():
        q1, q3= np.percentile(v,[25,75])
        irq = q3 - q1
        v_col = v[(v <= q1 - 1.5 * irq) | (v >= q3 + 1.5 * irq)]
        perc = np.shape(v_col)[0] * 100.0 / np.shape(housing)[0]
        print("Outliers of %s Column = %.2f%%" % (k, perc))
print("************************************************************************")

# HER KOLONDAKİ VERİ DAĞILIMINI GÖRSELLEŞTİRME

fig, axs = plt.subplots(ncols=7, nrows=2, figsize=(20, 10))
index = 0
axs = axs.flatten()
for k,v in housing.items():
    sns.boxplot(y=k, data=housing, ax=axs[index])
    index += 1

# BAĞIMSIZ(y) VE BAĞIMLI(x) DEĞİŞKENLERİ AYIRMA

x = housing.iloc[:,:12]
y = housing.iloc[:,12:]


# TEST VE TRAIN VERİLERİMİZİ OLUŞTURMA

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)

print(x_train.head())
print(y_train.head())

# RANDOM FOREST REGRESSION METHODU

from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators=10, random_state=5)
rf.fit(x_train, y_train)
predicted = rf.predict(x_test)

y_test_np = y_test.iloc[:,0:].values
pre2 =np.transpose([predicted])

# POLYNAMIAL REGRESSION METHODU

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

poly_reg = PolynomialFeatures(degree = 3)
x_poly = poly_reg.fit_transform(x)


lin_reg = LinearRegression()
lin_reg.fit(x_poly,y)
y_pred = lin_reg.predict(x_poly)
y_np = y.values

# YAPTIRDĞIMIZIN TAHMİNLERİN DOĞRULUĞUNU R2 SCORE METHODU İLE ÖLÇME

from sklearn.metrics import r2_score

r2s_rfm = r2_score(y_test_np, pre2)
r2s_pr = r2_score(y_np, y_pred)
print("R2 Score of Random Forest Regression Model: ", r2s_rfm)
print("R2 Score of Polynomial Regression Model: ", r2s_pr)

'''
SONUÇ

R2 değerleri ortaya gösteriyorki bu data setinde polynamial regression methodu,
random forest regression methoduna göre daha başarılı tahminler üretiyor.
 
'''