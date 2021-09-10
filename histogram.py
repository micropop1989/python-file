import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(170, 10, 250)
y1 = np.array([155, 170, 190, 200, 210])
y2 = np.array([10, 20, 40, 50, 60])

plt.suptitle('big title')

plt.subplot(1, 2, 1)
plt.title("title 1")
plt.xlabel("x1 label")
plt.ylabel("y1 label")
plt.plot(y1, y2, marker = '*')
plt.grid()

plt.subplot(1, 2, 2)
plt.title("title 2")
plt.xlabel("x1 labe2")
plt.ylabel("y1 labe2")
plt.hist(x)
plt.grid()


plt.show()
