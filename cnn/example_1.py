# decide loss function
# decide optimizer
# train
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Conv2D, InputLayer, MaxPooling2D, Flatten, Dense

# no need for split
from keras.optimizers import Adam
from keras.utils import to_categorical

(x_train, y_train), (x_test, y_test) = mnist.load_data()
y_train = to_categorical(y_train)
print(y_train[0])

model = Sequential()

model.add(Conv2D(32, kernel_size=(5, 5), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D())  # 2,2
model.add(Conv2D(16, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D())  # 2,2
model.add(Flatten())
model.add(Dense(50, activation='relu'))
model.add(Dense(10, activation='softmax')) #categorical porplem
opt = Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
model.fit(x_train, y_train,epochs=10)
