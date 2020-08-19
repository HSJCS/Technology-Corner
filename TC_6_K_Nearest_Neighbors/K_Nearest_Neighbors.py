from sklearn.neighbors import KNeighborsClassifier

x = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(x, y)

print(classifier.predict([[1.1]]))

print(classifier.predict_proba([[0.9]]))

