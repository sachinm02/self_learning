# Importing various modules
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pandas as pd
import pickle

# Reading the data file
data = pd.read_csv('iris.data',header=None)
print(data.head())

# Creating Independent and Dependent Variables
X = data.iloc[:,0:4].values
y = data.iloc[:,4].values

# Performing label encoding on our categorical target column
le = LabelEncoder()
y_transformed = le.fit_transform(y)

# Checking the mapping of our classes
data['encoded'] = le.fit_transform(data[4].values)
print(data.drop_duplicates(4))

# Splitting our dataset into training and testing datasets
x_train,x_test,y_train,y_test = train_test_split(X,y_transformed,test_size=0.25,random_state=42)

# Initialising our classifier and fitting training data on it
model = SVC(kernel='linear').fit(x_train,y_train)

# Getting predictions of our test data using our classifier
pred = model.predict(x_test)

# Printing classification report for checking performance of our classifier on each class
from sklearn.metrics import classification_report
print(classification_report(y_test,pred))

# Dumping/Saving our model for later use
pickle.dump(model,open('model.pkl','wb'))