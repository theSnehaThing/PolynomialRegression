#POLYNOMIAL REGRESSION
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

#fitting
from sklearn.preprocessing import PolynomialFeatures
regressor_poly = PolynomialFeatures(degree=4)
X_poly = regressor_poly.fit_transform(X)
from sklearn.linear_model import LinearRegression
regressor_lin = LinearRegression()
regressor_lin.fit(X_poly, y)

#predcting
regressor_lin.predict(regressor_poly.fit_transform([[6.5]]))

#Visualising
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor_lin.predict(regressor_poly.fit_transform(X_grid)), color = 'blue')
plt.title('Truth or Bluff')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

