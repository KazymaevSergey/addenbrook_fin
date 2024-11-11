# Класс для предсказания
from catboost import CatBoostClassifier
import joblib



class Predict_ace_cat():
    def __init__(self, model_catboost):
        
        self.clf = CatBoostClassifier().load_model(model_catboost)  #загрузка сохраненно     модели

    def predict(self, sample):
        return self.clf.predict(sample)
    
    def predict_proba(self, sample): 
        return self.clf.predict_proba([sample])
    
    def clf_classes(self):
        return self.clf.classes_

#loaded_model = joblib.load(filename)
    
class Predict_ace_svm():
    def __init__(self, model_svm):
        
        self.clf = joblib.load(model_svm)

    def predict(self, sample):
        return self.clf.predict([sample])
    
    def predict_proba(self, sample): 
        return self.clf.predict_proba([sample])
    
    def clf_classes(self):
        return self.clf.classes_
    
class Predict_ace_pkl():
    def __init__(self, model):
        
        self.clf = joblib.load(model)

    def predict(self, sample):
        return self.clf.predict(sample)
    
    def predict_proba(self, sample): 
        return self.clf.predict_proba(sample)
    
    def clf_classes(self):
        return self.clf.classes_
    
    
    



















    
        
    
