import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import model_selection
from sklearn.metrics import accuracy_score
import joblib

st.title('My Test Classification app')


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

array = dataset.values
X = array[:,0:4] # Select Sepal and Petal lengths and widths
Y = array[:,4] # Select class
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(
    X, Y, test_size = validation_size, random_state = seed)

log_reg = LogisticRegression()
log_reg.fit(X_train, Y_train)
predictions = log_reg.predict(X_validation)
acc_score = accuracy_score(Y_validation, predictions)

# Dump the model into a folder

joblib.dump(log_reg, "model/log_reg.pkl")

# Use the model for predictions

# Load the model back
model= open("model/log_reg.pkl", "rb")
log_reg_clf=joblib.load(model)

input_vars = [6.5, 3.2, 5.1, 2.0]
log_reg_clf.predict([input_vars])


#Create 5 sliders for the 5 inputs


input_columns = list(dataset.columns)[:4]
input_selection = []
for i in input_columns : 
    st.write("\n")
    values = st.slider(i, 0.0, 10.0, 0.1)
    input_selection.append(values)
    st.write(f"The selection of {i} is {values}\n")

#input_selection

if st.button('Click here to get predictions'):
    st.write('Computing predictions .....')
    st.write(f"Your selection could most probably be {log_reg_clf.predict([input_selection])[0]}")

else:
    st.write('Nothing pressed')