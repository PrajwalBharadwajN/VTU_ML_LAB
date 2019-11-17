from sklearn import datasets,metrics
iris = datasets.load_iris()

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(iris.data,iris.target)

from sklearn.cluster import KMeans
model1 =KMeans(n_clusters=3)
model1.fit(X_train,y_train)
print("K-means: ",metrics.accuracy_score(y_test,model1.predict(X_test)))

from sklearn.mixture import GaussianMixture
model2 = GaussianMixture(n_components=3)
model2.fit(X_train,y_train)
print("EM: ",metrics.accuracy_score(y_test,model2.predict(X_test)))