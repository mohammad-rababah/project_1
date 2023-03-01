# linear regrssion -> house price
# binery classifcation -> diabets
# category
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.utils import to_categorical

(x_train, y_train), (x_test, y_test) = mnist.load_data()
# more than one cateogry
# input layer
# ....
# ....
# ..
# output layer -> sigmoid ---> 0,1 , thanh --> [-1,1] , liner->(R)
# 10 outputs ---- > mos propablty
# y = 0,1,2,3....9
# y0 .... y9
print(y_train[0])
# [0,0,0,0,0,1,0,0,0,0] one hot encoding  --- > 5
# [0,0,0,0,1,0,0,0,0,0] ---> 4
y_train = to_categorical(y_train)
print(y_train[0])