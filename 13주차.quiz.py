import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

filename = "./data/09_irisdata.csv"
columns = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
data = pd.read_csv(filename, names=columns)
print(data.shape)
print(data.describe())
print(data.groupby('class').size())
scatter_matrix(data)
plt.savefig("./data/scatter_plot.png")

X = data.iloc[:, 0:4].values
Y = data.iloc[:, 4].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=41)
model = DecisionTreeClassifier()
kfold = KFold(n_splits=10, random_state=5, shuffle=True)
results = cross_val_score(model, X, Y, scoring='accuracy', cv=kfold)
print(results.mean())
