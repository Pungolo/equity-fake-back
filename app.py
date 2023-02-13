import json
import numpy as np
import pandas as pd
import requests
from pandas import json_normalize
import logging
import excel2json as ex
import openpyxl
from flask import Flask, Response, jsonify, make_response, request
import time

pd.options.mode.chained_assignment = None  # pandas option config

app = Flask(__name__)


@app.route("/liveness", methods=['GET'])
def livenesses():
    return Response(status=200, mimetype='application/json')


@app.route("/readiness", methods=['GET'])
def readiness():
    return Response(status=200, mimetype='application/json')


@app.route("/save", methods=['POST'])
def getJson():
    with open("RequestEquity.json") as json_file:
        json_data = json.load(json_file)
    print(json_data)
    # j = pd.read_json("C:\\Users\\Luciano Degni\\Documents\\flaskProject\\ResponseEquitytrs.json")
    #h = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    #r = requests.get('http://localhost:8080/flussi/saveDocument?type=insert', json=json_data, headers=h)
    # print(f"Status Code: {r.status_code}, Response: {r.json()}")
    # return f"Status Code: {r.status_code}, Response: {r.json()}"
    #r = requests.get("http://localhost:8080/flussi/getDocument?collection=EquityTRS&dataRiferimento=20220824&basketID=EquityTRS_20220824161257&version=0", headers=h)
    return json_data#r.json()

@app.route("/update", methods=['POST'])
def getJsonControlli():
    with open("ResponseEquitytrs.json") as json_file:
        json_data = json.load(json_file)
    print(json_data)
    # j = pd.read_json("C:\\Users\\Luciano Degni\\Documents\\flaskProject\\ResponseEquitytrs.json")
    h = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    #r = requests.get('http://localhost:8080/flussi/saveDocument?type=update', json=json_data, headers=h)
    # print(f"Status Code: {r.status_code}, Response: {r.json()}")
    # return f"Status Code: {r.status_code}, Response: {r.json()}"
    #r = requests.get("http://localhost:8080/flussi/getDocument?collection=EquityTRS&dataRiferimento=20220824&basketID=EquityTRS_20220824161257&version=0", headers=h)
    return json_data#r.json()


# @app.route("/getXlsx", methods=['POST'])
# def remoteExecute():
#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s %(levelname)s [%(module)s] (%(threadName)s) %(message)s',
#                         datefmt='%Y-%m-%d %H:%M:%S.000%z')
#     logging.info('Inizio Richiesta !!!!')
#
#     excelData = pd.read_excel("C:\\Users\\Luciano Degni\\Downloads\\ORIG_Equity_TRS_20220802 (1).xlsx", sheet_name='Foglio1')
#     jsonStr = excelData.to_json()

    # read_file = pd.read_excel(r"C:\Users\Luciano Degni\Downloads\ORIG_Equity_TRS_20220802 (1).xlsx")
    # csv = read_file.to_csv(r"C:\Users\Luciano Degni\Downloads\ORIG_Equity_TRS_20220802 (1).xlsx", index=None, header=True)

    # csvJson = csv.to_json()

    # excelData2 = ex.convert_from_file("C:\\Users\\Luciano Degni\\Downloads\\ORIG_Equity_TRS_20220802 (1).xlsx", "C:\\Users\\Luciano Degni\\Downloads\\test.json")

    # print(excelData2)
    return jsonStr


if __name__ == "__main__":
    #app.run(host="0.0.0.0", port="8000", debug=True)
    app.run()
