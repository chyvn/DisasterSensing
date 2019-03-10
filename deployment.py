from sklearn.externals import joblib

loaded_model = joblib.load('./model_file.sav')
result = loaded_model.predict([[50, 50, 50, 50]])
print(result)
