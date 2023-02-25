import pandas as pd
from keras import Sequential
from keras.layers import InputLayer, Dense
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, Normalizer

df = pd.read_csv('diabetes.csv')
scaler = MinMaxScaler()
X = df.drop(columns="Outcome")
norm = Normalizer()
for c in X.columns:
    df[c] = scaler.fit_transform(df[c].values.reshape(-1, 1))
    df[c] = norm.fit_transform(df[c].values.reshape(-1, 1))

print(df.head())
train_df, test_df = train_test_split(df, test_size=0.20)

train_df = pd.DataFrame(train_df)
train_x = train_df.drop(columns=["Outcome"], axis=1)
train_y = train_df['Outcome']

# build the model
model = Sequential()
model.add(InputLayer(input_shape=train_x.shape[1]))  # 8 ,1
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile
opt = Adam(learning_rate=0.000001)
model.compile(optimizer=opt, loss='binary_crossentropy'
              , metrics=['accuracy'])
model.fit(train_x, train_y, validation_split=0.2, epochs=100)
