from encodings import normalize_encoding
from locale import normalize
from sklearn.datasets import load_iris
from sklearn import preprocessing
iris=load_iris()
print(iris.data.shape)
X=iris.data
Y=iris.target
normalize_X=preprocessing.normalize(X)