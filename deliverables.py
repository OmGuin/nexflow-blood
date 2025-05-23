import pickle
from featureimportance import get_feature_importance
from hyperparameter_tuning.data import get_data
from eval import evaluate

X_train, X_test, y_train, y_test = get_data()

#TRAINED RANDOM FOREST MODEL
with open("rf_model.pkl", 'rb') as file:
    rf_model = pickle.load(file)

#BASELINE TRAINED LOGISTIC REGRESSION MODEL
with open("lgr_model.pkl", 'rb') as file:
    lgr_model = pickle.load(file)

#TRAINED XGBOOST MODEL
with open("xgb_model.pkl", 'rb') as file:
    xgb_model = pickle.load(file)



get_feature_importance("RF", X_train)
get_feature_importance("XGB", X_train)


evaluate(X_test, y_test, "RF")
evaluate(X_test, y_test, "XGB")




