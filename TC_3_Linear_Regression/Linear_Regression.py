import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])

# y = 1 * x_0 + 2 * x_1 + 3
y = np.dot(x, np.array([1, 2])) + 3

regression = LinearRegression().fit(x, y)
regression.score(x, y)

regression.coef_
regression.intercept_

regression.predict(np.array([[3, 5]]))
