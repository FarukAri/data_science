import pandas as pd

# df = pd.DataFrame()
# df = pd.DataFrame([1, 2, 3, 4])

data = [["Tolga",50], ["Gökay",45], ["Faruk", 90], ["Ali", 10]]
df = pd.DataFrame(data, columns=["Name", "Grade"], index=[1, 2, 3, 4], dtype=float)
# print(df)

# Another way with using dictionary method

dict = {"Name":["Faruk", "Tolga", "Gökay"], "Grades":[99, 45, 10]}
df2 = pd.DataFrame(dict, index=[2979, 2986, 2991])
# print(df2)

# or

dict_list = [
    {"Name":"Faruk", "Grades":99},
    {"Name":"Tolga", "Grades":73},
    {"Name":"Gökay", "Grades":12}
]

df3 = pd.DataFrame(dict_list, index= [11, 22, 35])
print(df3)







# s1 = pd.Series([3, 4, 6, 8])
# s2 = pd.Series([3, 4, 9, 5])

# data = dict(apples = s1, oranges = s2)
# df = pd.DataFrame(data)


# # print(data)
# print(df)