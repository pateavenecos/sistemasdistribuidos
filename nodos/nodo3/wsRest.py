from flask import Flask
from flask import jsonify
from flask import request

from urllib import response
import requests

app = Flask(__name__)

#Fuse----

vecinos=[
 {
 'ip':'172.17.0.2',
 'port':'2000',
 'pathGetNum':'/nodo/getNum',
 'pathGetSum':'/nodo/getSum'
 }
 ]

@app.route('/nodo/getNum',methods=['GET'])
def getNum():
    return jsonify({'r':"30"})

@app.route('/nodo/getSum',methods=['GET'])
def getSum():
    response1={'r':'0'}
    if(request.remote_addr!=vecinos[0]["ip"]):
        response1 = requests.get("http://"+vecinos[0]["ip"]+":"+vecinos[0]["port"]+vecinos[0]["pathGetSum"])
    
    sum=int(response1['r'])+30
    print (sum)
    return jsonify({'r':sum})



if __name__ == '__main__':
 app.run(host="172.17.0.4", port=2000)
