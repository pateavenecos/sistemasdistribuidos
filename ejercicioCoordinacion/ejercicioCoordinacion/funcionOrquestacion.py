def receive():
    a= int(request.json['a'])
    b= int(request.json['c'])
    c= int(request.json['d'])
    d= int(request.json['c'])

    #((a+b)-c)*d
    #Hablar con B
    response = requests.post("http://"+Aaddress+":"+port+"/coord/sum", json={"a":a,"b":b})
    rA=response.json()
    #Hablar con D
    response = requests.post("http://"+Daddress+":"+port+"/coord/abst", json={"a":rA['sum'],"c":c})
    rD=response.json()
    #Hablar con C
    response = requests.post("http://"+Caddress+":"+port+"/coord/mult", json={"a":rD['abst'],"d":d})


    resp=0

    resp=a**b
    return jsonify({'pow':resp})
