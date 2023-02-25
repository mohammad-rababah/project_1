import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('car data.csv')
df.info()
print(df.describe())

#df["Selling_Price"].plot()  # matplot
df["Year"].hist()
df.plot.scatter(x="Year", y="Selling_Price")


plt.show()

# dic = {
#     "X": [-1, -5, -6, 6, 7],
#     "Y": [-1, -4, -2, 3, 9]
# }
# df2 = pd.DataFrame(dic)
# print(df2.head())
# df2.info()
# df2.plot.scatter(x="X", y="Y")
# plt.show()
