from base64 import decode
from flask import Flask
from flask import jsonify
from flask import request

import json

from urllib import response
import requests

app = Flask(__name__)

#Rampart----

vecinos=[
 {
 'ip':'172.17.0.3',
 'port':'2000',
 'pathGetNum':'/nodo/getNum',
 'pathGetSum':'/nodo/getSum'
 },
 {
 'ip':'172.17.0.4',
 'port':'2000',
 'pathGetNum':'/nodo/getNum',
 'pathGetSum':'/nodo/getSum'

 }
 ]

@app.route('/nodo/getNum',methods=['GET'])
def getNum():
    print("http://"+vecinos[0]["ip"])
    return jsonify({'r':"10"})

@app.route('/nodo/getSum',methods=['GET'])
def getSum():
    response1={'r':'0'}
    response2={'r':'0'}
    i=0
    sum=0
    while i<2:
        if(request.remote_addr!=vecinos[i]["ip"]):
            response1 = requests.get("http://"+vecinos[i]["ip"]+":"+vecinos[i]["port"]+vecinos[i]["pathGetSum"])
            sumx=response1.json()
            sum=sum+int(sumx['r'])
            print(sumx['r'])

        i+=1
    return jsonify(sum)

if __name__ == '__main__':
 app.run(host="172.17.0.2", port=2000)
