# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Importing libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#read the data
dataset = pd.read_csv('Data.csv')
X= dataset.iloc[:,:-1].values
X
Y= dataset.iloc[:,0].values
Y

#deal with the missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer=imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])
X


#Encoding Categorical Data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
X
#Using dummy variables
columnTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [0])],remainder='passthrough')
X=np.array(columnTransformer.fit_transform(X),dtype=np.str)
X
labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)

#Splitting the data into training set and test set
from sklearn.model_selection import train_test_split
X_train, Y_train, X_test, Y_test = train_test_split(X,Y,test_size =0.2, random_state =0)

##Feature scaling
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
X_train=sc_x.fit_transform(X_train)
X_test=sc_x.transform(X_test)

