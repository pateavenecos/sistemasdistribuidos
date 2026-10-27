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

@app.route('/coord/sum',methods=['POST'])
def sum():
    print("a"+ str(request.json['a']))
    print("b"+ str(request.json['b']))
    print("c"+ str(request.json['c']))

    a= int(request.json['a'])
    b= int(request.json['b'])
    c= int(request.json['c'])
    #sum a+b
    sumab = int(a) + int(b)

    #talk with C
    responseC = requests.post("http://"+Caddress+":"+port+"/coord/subst", json={"sumab":sumab,"c":c})
    rC=responseC.json()
    #return the result    
    return jsonify({'resp':rC['resp']})
    

if __name__ == '__main__':
    print("B runing")
    app.run(host="0.0.0.0", port=5000)