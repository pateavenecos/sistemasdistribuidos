from flask import Flask
from flask import jsonify
from flask import request
import requests

app = Flask(__name__)

#----address of others ws.
Aaddress = "172.18.0.2"
Baddress = "172.18.0.3"
Caddress = "172.18.0.4"
Daddress = "172.18.0.5"
#----address of this ws.
port= "5000"

@app.route('/coord/operate',methods=['POST'])
def operate():
    a= int(request.json['a'])
    b= int(request.json['b'])
    c= int(request.json['c'])
    d= int(request.json['d'])
    
    #((a+b)-c)*d
    #talk with B and C
    responseB = requests.post("http://"+Baddress+":"+port+"/coord/sum", json={"a":a,"b":b,"c":c})
    rB=responseB.json()
    #talk with D
    responseD = requests.post("http://"+Daddress+":"+port+"/coord/mult", json={"respB":rB['resp'],"d":d})
    rD=responseD.json()
        
    return jsonify({'finalResp':rD['resp']})

if __name__ == '__main__':
    print("A runing")
    app.run(host="0.0.0.0", port=5000)