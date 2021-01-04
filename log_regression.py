from sklearn import datasets
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
iris= datasets.load_iris()

# print(list(iris.keys()))
# print(iris['data'])
# print(iris['target'])
# print(iris['DESCR'])
# print(iris['data'].shape)

x = iris['data'][:, 3:]
y= (iris['target'] == 2).astype(np.int)
# print(y)
# print(x)
# fiting a log regression classifier to check if a flower is iris verginica or not

clf = LogisticRegression()
clf.fit(x, y)

eg= clf.predict(([[2.6]]))
print(eg)

# using matplotlib to pot the visualisation
x_new = np.linspace(0,3,1000).reshape(-1,1)
# print(x_new)
y_prob = clf.predict_proba(x_new)
plt.plot(x_new, y_prob[:,1], "g-", label='verginica')
plt.show()