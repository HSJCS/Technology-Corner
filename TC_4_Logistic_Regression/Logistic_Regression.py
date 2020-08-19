from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

x, y = load_iris(return_x_y=True)

classifier = LogisticRegression(random_state=0).fit(x, y)

classifier.predict(x[:2, :])
classifier.predict_proba(x[:2, :])

classifier.score(x, y)
