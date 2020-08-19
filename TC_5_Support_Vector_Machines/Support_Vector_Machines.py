from sklearn import svm

x = [[0, 0], [1, 1]]
y = [0, 1]

classifier = svm.SVC()

classifier.fit(x, y)

classifier.predict([[2., 2.]])