# from app.l_model import cardio

# if __name__ == '__main__':
#     cardio()
#     print('Model and Scalar trained, saved successfully.')


from app.svm_models import svm_cardio

if __name__ == '__main__':
    print('Training SVM model and scaler...')
    svm_cardio()
    print('SVM Model and Scaler trained & saved successfully to models/svm/!')


# run - > python train_model.py for converting to binary file of models