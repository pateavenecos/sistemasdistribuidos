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

@app.route('/coord/subst',methods=['POST'])
def subst():
    print("sumab:"+ str(request.json['sumab']))
    print("c:"+ str(request.json['c']))

    sumab= int(request.json['sumab'])
    c= int(request.json['c'])
    #substract sumab-c
    subst = sumab-c
    #return the result    
    return jsonify({'resp':subst})

if __name__ == '__main__':
    print("C runing")
    app.run(host="0.0.0.0", port=5000)