#cmd
#py get-pip.py
#cd C:\Users\lcg\AppData\Local\Programs\Python\Python38-32\Scripts
#pip install matplotlib
#pip install seaborn
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000), hist=False)

plt.show()
