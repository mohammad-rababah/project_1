import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('diabetes.csv')
train, test = train_test_split(df, shuffle=True, test_size=0.2)
train = pd.DataFrame(train)

train.drop(columns=["Outcome"], inplace=True, axis=1)
test = pd.DataFrame(test)
test = test["Outcome"]

model = LogisticRegression(max_iter=10000)
model.fit(train, test)
