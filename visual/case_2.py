# wrong format
import pandas as pd

df = pd.read_csv("car data.csv")
df.info()
# column ->Selling_Price
# cahnge  Selling_Price type
df['string'] = df['Selling_Price'].astype(str)
df.info()

df['selling_price_2'] = pd.to_numeric(df['string'])
df['selling_price_2'] = df['string'].astype(float)

df['max'] = df['Selling_Price'] * 2
df.insert(0, "MAX", df['Selling_Price'] * 2)
print(df.head())
df.info()
