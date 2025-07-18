# -*- coding: utf-8 -*-
"""Loan Status prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1w1ozzeDNCowcwcenuf1aWaX36XhrWgAX

Importing the Dependencies
"""

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""Data Collection & Processing"""

# loading the dataset to pandas DataFrame
loan_dataset = pd.read_csv('/content/train_u6lujuX_CVtuZ9i (1).csv')

type(loan_dataset)

# printing the first five rows
loan_dataset.head()

# printing the last 5 rows
loan_dataset.tail()

# number of rows and columns
loan_dataset.shape

# statistical measures
loan_dataset.describe()

# number of missing values in each column
loan_dataset.isnull().sum()

# dropping the missing values
loan_dataset = loan_dataset.dropna()

# number of missing values in each column
loan_dataset.isnull().sum()

# label encoding
loan_dataset.replace({"Loan_Status":{'N':0,'Y':1}},inplace=True)

# printing the first five rows
loan_dataset.head()

# dependent column values
loan_dataset['Dependents'].value_counts()

# replacing the value 3+ to 4
loan_dataset = loan_dataset.replace(to_replace='3+', value=4)

"""Data Visualization"""

# education & Loan Status
sns.countplot(x='Education',hue='Loan_Status',data=loan_dataset)

# marital status & loan status
sns.countplot(x='Married',hue='Loan_Status',data=loan_dataset)

# convert categorial values to numerical values
loan_dataset.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},'Self_Employed':{'No':0,'Yes':1},'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)

# printing the first five rows
loan_dataset.head()

# seperating the data & label
X = loan_dataset.drop(columns=['Loan_ID','Loan_Status'],axis=1)
Y = loan_dataset['Loan_Status']
print(X)
print(Y)

"""Train Test Split"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=2)

print(X.shape,X_train.shape,X_test.shape)

"""Training the model:
Support Vector Machine Model
"""

classifier = svm.SVC(kernel='linear')

# training the support vector machine model
classifier.fit(X_train,Y_train)

"""Model Evaluation"""

# accuracy score on training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction,Y_train)

print('Accuracy on training data : ',training_data_accuracy)

# accuracy score on test case
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction,Y_test)

print('Accuracy on test data : ',test_data_accuracy)

"""Making a Predictive System"""

# prompt: make this predictive system code

import numpy as np
input_data = (1,1,1,0,0,2583,2358.0,120.0,360.0,1.0,2) # Removed the extra value

# change input data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the numpy array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = classifier.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person is not eligible')
else:
  print('The person is eligible')

