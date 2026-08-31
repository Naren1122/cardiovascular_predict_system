import joblib

MODEL_PATH = 'models/svm/svm_cardio_model.pkl' 

SCALAR_PATH = 'models/svm/svm_scaler.pkl' 


def load_svm_model():
    svm_model = joblib.load(MODEL_PATH)
    svm_scaler = joblib.load(SCALAR_PATH)
    return svm_model, svm_scaler












# import pandas as pd
# import joblib # to convert ML models to binary format

# from sklearn.svm import SVC
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import classification_report, confusion_matrix

# df = pd.read_csv('data/Cardiovascular_Disease.csv')

# age_data = (df['age']/365).astype(int)
# df['age'] = age_data

# data_filter = df[(df['height'].between(125,200)) & (df['weight'].between(40,120)) & (df['ap_hi'].between(100,200)) & (df['ap_lo'].between(50,90))]
# df = data_filter

# MODEL_PATH = 'models/svm/svm_cardio_model.pkl' # model path
# SCALAR_PATH = 'models/svm/svm_scaler.pkl' # scaler path

# def svm_cardio():
#     svm_feature = ['age','gender','height','weight','ap_hi','ap_lo','cholesterol','gluc','smoke','alco','active']
#     target = 'cardio'
    
#     X = df[feature]
#     Y = df[target]
    
#     X_train, X_test, Y_train, Y_test = train_test_split(
#     X,Y,test_size=0.2, random_state=42,  stratify = Y
# )
    
#     svm_scaler = StandardScaler()
#     X_train_scale = scaler.fit_transform(X_train)
#     X_test_scale = scaler.transform(X_test)
    
#     svm_model = SVC()
    
#     model.fit(X_train_scale,Y_train)
#     model.predict(X_test_scale)
    
#     # these are not required in production
#     # Y_pred = model.predict(X_test_scale)
    
#     # cr = classification_report(Y_test, Y_pred , output_dict=True)
#     # cm = confusion_matrix(Y_test , Y_pred)
#     joblib.dump(model, MODEL_PATH)
#     joblib.dump(scaler, SCALAR_PATH)
   
    
#     return svm_feature, svm_scaler, svm_model