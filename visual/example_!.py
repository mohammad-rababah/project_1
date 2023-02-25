import matplotlib.pyplot as plt

X1 = [1, 2, 3, 4, 5, 6]
Y1 = [2, 4, 6, 18, 12, 12]
X2 = [2, 7, 8, 9]
Y2 = [6, 7, 9, 2]
plt.plot(X1, Y1,linestyle='v')
plt.plot(X2, Y2)
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Test", fontsize=20, color='red')
plt.show()
