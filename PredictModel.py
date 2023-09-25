import pickle
import gzip
import numpy as np

with gzip.open('./AMSModel.pgz','r') as f:
    Model = pickle.load(f)

def PredictAlarm(data):
    pred = Model.predict(data)[0]
    return pred