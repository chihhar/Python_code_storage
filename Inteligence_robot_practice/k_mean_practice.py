import numpy as np
import urllib.request
from sklearn.neighbors import KNeighborsClassifier

train_num=int(X.shape[0]*0.8)
np.random.seed(42)
#最近傍法ならk=1
n_neighbors=1

#url with dataset
url ="https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"

#download the file
raw_data = urllib.request.urlopen(url)
#load the CSV ffile as a numpy matrix
dataset = np.loadtxt(raw_data, delimiter=",")

#separate data into input and label
all_X = dataset[:,1:14]
all_y = dataset[:,0]
#separate data into traindata and testdata
perm = np.random.permutation(X.shape[0])
randX=all_X[perm]
randy=all_y[perm]

#train knn
knn = KNeighborsClassifier(n_neighbors=n_neighbors)
knn.fit(randX[:train_num],randy[:train_num])

#testdata's score
print("test score:"+str(knn.score(randX[train_num:],randy[train_num:])*100)+"%")
#traindata's score
print("train score:"+str(knn.score(randX[:train_num],randy[:train_num])*100)+"%")
