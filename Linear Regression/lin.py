import matplotlib.pyplot as plt
plt.style.use('ggplot')
import pandas as pd
import seaborn as sns
import numpy as np

plt.rcParams['figure.figsize'] = (12, 8)    # setting a default figure size
data = pd.read_csv('bikedata.txt')  # loading the data
# print(data.head())      # for printing first 5 entries
# print(data.info())      # for metadata of dataset

ax = sns.scatterplot(x="Population", y="Profit", data=data)
ax.set_title("profit vs population")
# plt.show()  # tells the system to draw the plot in Pycharm

def costfunc(X,y,theta):
    m = len(y)
    ypred = X.dot(theta)
    eror = (ypred - y) ** 2
    return 1/(2 * m) * np.sum(eror)

m = data.Population.values.size
X = np.append(np.ones((m, 1)), data.Population.values.reshape(m, 1), axis=1)    #  appending 1 column vector to X
y = data.Profit.values.reshape(m, 1)
theta = np.zeros((2, 1))    # matrix of 2R 1C
J = costfunc(X, y, theta)
#   print(J)

#   gradient descent
def gdes(X, y, theta, alpha, iter):
    m= len(y)
    costs =[] #  stores history of j(theta) values
    for i in range(iter):
        ypred =  X.dot(theta)
        eror = np.dot(X.transpose(), (ypred - y))
        theta -= 1/m * alpha * eror
        costs.append(costfunc(X, y, theta))
    return theta, costs

theta, costs =gdes(X, y, theta, alpha=0.01, iter=2000)
print(theta)

plt.plot(costs)     #  plotting the convergence graph
axes = plt.gca()
axes.set_ylim([4, 7])
plt.xlabel("iterations")
plt.ylabel("$J(\Theta)$")
#   plt.show()

theta= np.squeeze(theta)
print(theta)
sns.scatterplot(x="Population", y="Profit", data=data)
x_val = [x for x in range(5, 25)]
y_val = [(theta[0] + theta[1]* x) for x in x_val]
sns.lineplot(x=x_val, y=y_val)
plt.show()

