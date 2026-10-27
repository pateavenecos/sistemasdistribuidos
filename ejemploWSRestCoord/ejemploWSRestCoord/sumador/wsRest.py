from flask import Flask
from flask import jsonify
from flask import request
import requests

app = Flask(__name__)

@app.route('/sumador/sumar',methods=['POST'])
def sumar():
    a=request.json["a"]
    b=request.json["b"]
    c=request.json["c"]
    d=request.json["d"]
    r=int(a)+int(b)
    dat={"r":r, "c":c, "d":d}
    response= requests.post("http://172.17.0.3:5000/restador/restar", json=dat)
    #return jsonify({'suma':r})
    return jsonify(response.json())


if __name__ == '__main__':
 app.run(host="172.17.0.2", port=5000)
