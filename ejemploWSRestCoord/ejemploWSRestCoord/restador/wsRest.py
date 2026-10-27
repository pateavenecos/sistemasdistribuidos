from flask import Flask
from flask import jsonify
from flask import request
import requests

app = Flask(__name__)

@app.route('/restador/restar',methods=['POST'])
def restar():
    r=request.json["r"]
    c=request.json["c"]
    d=request.json["d"]
    r1=int(r)-int(c)
    dat={"r1":r1, "d":d}
    response= requests.post("http://172.17.0.4:5000/multiplicador/multiplicar", json=dat)
    #return jsonify({'resta':r1})
    return jsonify(response.json())

if __name__ == '__main__':
 app.run(host="172.17.0.3", port=5000)
