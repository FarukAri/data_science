from unittest import result
import pandas as pd

data = pd.read_csv("Seasons_Stats.csv")

data["Player"] = data["Player"].str.upper()
data["Index"] = data["Player"].str.find("a")
data =data[data.Name.str.contains("Jordan")]

print(data)
# print(data.columns)
