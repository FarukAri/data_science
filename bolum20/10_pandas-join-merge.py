import pandas as pd

customers = { 
    "CustomerID" : [1, 2, 3, 4],
    "Name" : ["Faruk", "Berke", "Mehmet", "Bedirhan"],
    "Surname" : ["Arı", "Albayrak", "Gülçin", "Pınar"]
}

orders = {
    "OrderID" : [10, 11, 12, 13],
    "CustomerID" : [1, 2, 5, 7],
    "OrderDate" : ["2015-5-4", "2015-8-3", "2014-9-12","2016-6-10"]
}

df_customers = pd.DataFrame(customers, columns=["CustomerID", "Name", "Surname"])
df_orders = pd.DataFrame(orders, columns=["OrderID", "CustomerID", "OrderDate"])

# print(df_customers)
# print(df_orders)

result = pd.merge(df_customers, df_orders, how="inner")     # Sadece kesişimleri olan verileri yazdırır.
result2 = pd.merge(df_customers, df_orders, how="left")     # Kesişim + Solda yazan df nin verilerini yazdırır.
result3 = pd.concat([df_customers, df_orders])              # Bütün veriler

# print(result)
# print(result2)
print(result3)

customersA = { 
    "CustomerID" : [1, 2, 3, 4],
    "Name" : ["Faruk", "Berke", "Mehmet", "Bedirhan"],
    "Surname" : ["Arı", "Albayrak", "Gülçin", "Pınar"]
}

customersB = { 
    "CustomerID" : [5, 6, 7, 8],
    "Name" : ["Furkan", "Berk", "Mert", "Barış"],
    "Surname" : ["Yılmaz", "Alkan", "Gümüş", "Aytaç"]
}


df_customersA = pd.DataFrame(customersA, columns=["CustomerID", "Name", "Surname"])
df_customersB = pd.DataFrame(customersB, columns=["CustomerID", "Name", "Surname"])

result = pd.concat([df_customersA, df_customersB])
print(result)