from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

#----address of others ws.
Aaddress = "172.18.0.2"
Baddress = "172.18.0.3"
Caddress = "172.18.0.4"
Daddress = "172.18.0.5"
#----address of this ws.
port= "5000"

@app.route('/coord/mult',methods=['POST'])
def mult():
    respB= int(request.json['respB'])
    d= int(request.json['d'])
    mult=respB*d
    return jsonify({'resp':mult})

if __name__ == '__main__':
    print("D runing")
    app.run(host="0.0.0.0", port=5000)