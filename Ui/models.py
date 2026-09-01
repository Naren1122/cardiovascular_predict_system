import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix


import os

# Dynamic path resolution: finds Cardiovascular_Disease.csv inside the same folder (Ui/)
_DIR = os.path.dirname(os.path.abspath(__file__))
_CSV = os.path.join(_DIR, 'Cardiovascular_Disease.csv')
if not os.path.exists(_CSV):
    _CSV = os.path.join('Ui', 'Cardiovascular_Disease.csv')
if not os.path.exists(_CSV):
    _CSV = 'Cardiovascular_Disease.csv'

df = pd.read_csv(_CSV)

age_data = (df['age']/365).astype(int)
df['age'] = age_data

data_filter = df[(df['height'].between(125,200)) & (df['weight'].between(40,120)) & (df['ap_hi'].between(100,200)) & (df['ap_lo'].between(50,90))]
df = data_filter

@st.cache_resource
def logistic_cardio():
    feature = ['age','gender','height','weight','ap_hi','ap_lo','cholesterol','gluc','smoke','alco','active']
    target = 'cardio'
    
    X = df[feature]
    Y = df[target]
    
    X_train, X_test, Y_train, Y_test = train_test_split(
    X,Y,test_size=0.2, random_state=42,  stratify = Y
)
    
    scaler = StandardScaler()
    X_train_scale = scaler.fit_transform(X_train)
    X_test_scale = scaler.transform(X_test)
    
    model = LogisticRegression(
    solver = 'lbfgs',
    class_weight = 'balanced',
    random_state = 42
)
    
    model.fit(X_train_scale,Y_train)
    Y_pred = model.predict(X_test_scale)
    
    cr = classification_report(Y_test, Y_pred , output_dict=True)
    cm = confusion_matrix(Y_test , Y_pred)
    
    return feature, scaler, model, Y_pred, cr, cm

@st.cache_resource
def svm_cardio(): 
     features = ['age' , 'gender' , 'height' , 'weight', 'ap_hi', 'ap_lo' , 'cholesterol', 'gluc', 'smoke' , 'alco' , 'active']
     target = 'cardio'  
     
     sampled_df = df.sample(n=5000, random_state=42)
     
     X = sampled_df[features]
     Y = sampled_df[target]
     
     X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state = 42, stratify = Y)
     
     scaler = StandardScaler()
     X_train_scale = scaler.fit_transform(X_train)
     X_test_scale = scaler.transform(X_test)
     
     model = SVC()
     model.fit(X_train_scale,Y_train)
     Y_pred = model.predict(X_test_scale)
     
     cr = classification_report(Y_test, Y_pred, output_dict=True)
     cm = confusion_matrix(Y_test, Y_pred)   
     
     return features, scaler, model, Y_pred, cr, cm