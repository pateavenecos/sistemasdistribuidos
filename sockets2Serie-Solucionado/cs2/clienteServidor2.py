import socket

def server_program():
    # get the hostname
    #host = socket.gethostname()
    host="172.17.0.3"
    port = 5000  # initiate port no above 1024
    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
    # configure how many client the server can listen simultaneously
    server_socket.listen(1)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    # receive data stream. it won't accept data packet greater than 1024 bytes
    data = conn.recv(1024).decode()
    print("from connected user: " + str(data))
    r="number1"
    #Here send request to next node
    r=r+client_program()
    #------------------------------
    conn.send(r.encode())  # send data to the client
    conn.close()  # close the connection

def client_program():
    #host = socket.gethostname()  # as both code is running on same pc
    host="172.17.0.4" #IP host server
    port = 5000  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    message = "getNumbers"
    client_socket.send(message.encode())  # send message
    data = client_socket.recv(1024).decode()  # receive response
    print('Received from server: ' + data)  # show in terminal
    client_socket.close()  # close the connection
    return data


if __name__ == '__main__':
    server_program()