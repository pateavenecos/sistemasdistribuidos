import socket
def client_program():
    #host = socket.gethostname()  # as both code is running on same pc
    host1="172.17.0.3"
    host2="172.17.0.4"
    host3="172.17.0.5"
    port = 5000  # socket server port number
    data=""
    client_socket1 = socket.socket()  # instantiate
    client_socket2 = socket.socket()  # instantiate
    client_socket3 = socket.socket()  # instantiate
    
    #to S1
    client_socket1.connect((host1, port))  # connect to the server
    message = "getNumber" # take input
    client_socket1.send(message.encode())  # send message
    data = data + client_socket1.recv(1024).decode()+","  # receive response
    print('Received from server: ' + data)  # show in terminal
    client_socket1.close()  # close the connection

    #to S2
    client_socket2.connect((host2, port))  # connect to the server
    message = "getNumber" # take input
    client_socket2.send(message.encode())  # send message
    data = data + client_socket2.recv(1024).decode()+","  # receive response
    print('Received from server: ' + data)  # show in terminal
    client_socket2.close()  # close the connection

    #to S3
    client_socket3.connect((host3, port))  # connect to the server
    message = "getNumber" # take input
    client_socket3.send(message.encode())  # send message
    data = data + client_socket3.recv(1024).decode()+","  # receive response
    r=data.split(",")
    sum=int(r[0])+int(r[1])+int(r[2])
    print(r)
    print(sum)
    print('Received from server: ' + data)  # show in terminal
    client_socket3.close()  # close the connection

if __name__ == '__main__':
    client_program()
