import numpy as np 
import pandas as pd
import sklearn
import matplotlib.pyplot as plt 
import image
import seaborn as sns
df = pd.read_csv('./data.csv')
#print(df)


#mean esperence etudiant en prive < etudiant etatique (<0.5)
#min valeur minimale
#max valeur maximale
#std écart type
#25% 50% 75% quantile
print(df.describe())
df['esprit'].value_counts()
print(
df['esprit'].value_counts())
plt.hist(df['esprit'].astype(int))
plt.savefig('testplot.png')
#image.open('testplot.png').save('testplot.jpg','JPEG')
g = sns.FacetGrid(df, col = 'esprit')
g.map(plt.hist,'skills_score',bins=30)
g.savefig("output.png")

#Modélisation:
X = df.iloc[:,[0,2,3,4,5]].values
y = df.iloc[:,1]
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.1)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)

classifier.fit(X_train,y_train)
test_1 = np.array([1,1,1,0,2.5]).reshape(1,-1)
#y_pred = classifier.predict(X_test)

y_test_1 = classifier.predict(test_1)
""" from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_test_1)
print(cm) """
print(y_test_1)

# Visualising the Training set results
""" from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 2].min() - 1, stop = X_set[:, 2].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 3].min() - 1, stop = X_set[:, 3].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 4].min() - 1, stop = X_set[:, 4].max() + 1, step = 0.01)
                     )
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Random Forest (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

plt.savefig("test.png") """

acc_random_forest = round(classifier.score(X_train,y_train)*100, 2)
print(acc_random_forest)

