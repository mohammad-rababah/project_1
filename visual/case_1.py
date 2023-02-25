# empty cells
import pandas as pd

df = pd.read_csv('car data.csv')
print(df[["Year","Kms_Driven","Fuel_Type"]].head())
df2 = df.dropna()
print(df[["Year","Kms_Driven","Fuel_Type"]].head())
print(df2[["Year","Kms_Driven","Fuel_Type"]].head())
print(df2.shape)

print(df[["Year", "Kms_Driven", "Fuel_Type"]].head())
df.dropna(inplace=True)

print(df[["Year", "Kms_Driven", "Fuel_Type"]].head())
df2 = df.fillna("kaled")
df.fillna("mohammad", inplace=True)
print(df[["Year", "Kms_Driven", "Fuel_Type"]].head())
