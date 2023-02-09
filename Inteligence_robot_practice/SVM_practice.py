import pandas as pd
import urllib.request
from sklearn.model_selection import train_test_split
from sklearn import svm

def prediction_binary(x):
  if x==" >50K":
    return 1
  else:
    return 0

#url with dataset
url ="https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
#download the file
raw_data = urllib.request.urlopen(url)

column_names=["age", "workclass","fnlwgt","education","education_num","marital_status","occupation","relationship","race","sex","capital_gain","capital_loss","hours_per_week","native_country","prediction"]
df =pd.read_csv(raw_data,names=column_names)

df["prediction_num"] = df.prediction.apply(prediction_binary)

pred_df = df.prediction_num
df2=df.drop(["prediction","fnlwgt","native_country","education","relationship","marital_status","occupation","capital_gain","capital_loss","workclass"],axis=1)
df3=df2.dropna(how="any")
df4=pd.get_dummies(df3)
df5 = df4[:10000]
train,test = train_test_split(df5)

y_train = (train.prediction_num).values
y_test = (test.prediction_num).values
X_train = (train.drop(["prediction_num"],axis=1)).values
X_test = (test.drop(["prediction_num"],axis=1)).values

svc_linear = svm.SVC(kernel='linear')
svc_linear.fit(X_train, y_train)
svc_poly = svm.SVC(kernel='poly' )
svc_poly.fit(X_train, y_train)
svc_rbf = svm.SVC(kernel='rbf' )
svc_rbf.fit(X_train, y_train)
print(svc_linear.score(X_test,y_test))
print(svc_rbf.score(X_test,y_test))
print(svc_poly.score(X_test,y_test))
