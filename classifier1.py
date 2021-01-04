# loading required modules 
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# loading datasets
iris = datasets.load_iris()

# printing description and features
# print(iris.DESCR)
features= iris.data
labels= iris.target
# print(features[0], labels[0]) printing first feature and label

# training the classifier
clf = KNeighborsClassifier()
clf.fit(features, labels)

preds = clf.predict([[1, 45, 23, 6.4]])
print(preds)
