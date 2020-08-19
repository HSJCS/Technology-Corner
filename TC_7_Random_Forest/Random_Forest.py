from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

x, y = make_classification(n_samples=1000, n_features=4,
                           n_informative=2, n_redundant=0,
                           random_state=0, shuffle=False)

classifier = RandomForestClassifier(max_depth=2, random_state=0)
classifier.fit(x, y)

print(classifier.predict([[0, 0, 0, 0]]))