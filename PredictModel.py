import pickle
import gzip
import numpy as np

with gzip.open('C:/Users/User/Desktop/Python_Practice/MaintenancePredict/AMSModel.pgz','r') as f:
    Model = pickle.load(f)

def PredictAlarm(data):
    pred = Model.predict(data)[0]
    return pred