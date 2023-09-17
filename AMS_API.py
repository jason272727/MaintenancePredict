import pandas as pd
import numpy as np
import PredictModel
from flask import Flask, request, jsonify
from flask_cors import CORS  #跨來源資源共享(讓網站存取不同來源的資源)


app = Flask(__name__) #API名稱
CORS(app) #讓大家可存取這個API

@app.route('/ReceiveDataFromEQP', methods=['POST'])
def GetData():
    Parameter = request.get_json()    
    ParameterValues = np.array(list(Parameter.values())) #轉成2D陣列
    inputData = np.column_stack(ParameterValues) #轉成2D陣列
    result = PredictModel.PredictAlarm(inputData)    
    return jsonify({'AlarmTypeResult':str(result)})   

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)