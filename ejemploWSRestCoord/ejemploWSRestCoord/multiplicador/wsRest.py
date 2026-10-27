from flask import Flask
from flask import jsonify
from flask import request
import requests

app = Flask(__name__)

@app.route('/multiplicador/multiplicar',methods=['POST'])
def multiplicar():
    r1=request.json["r1"]
    d=request.json["d"]
    r2=int(r1)*int(d)
    #dat={"r2":r2}
    #response= requests.post("http://172.17.0.4:5000/dividor/dividir", json=dat)
    return jsonify({'resp':r2})


if __name__ == '__main__':
 app.run(host="172.17.0.4", port=5000)
