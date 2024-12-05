import socket
"""
$ = success, ! = warning, * = announcement
to-do list:
1.making the start function (done)
2.making the receive choose function
3.broadcasting and receiving
"""
#setting up the server(socket, ip address, port, ADDR)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # server socket
IP = socket.gethostbyname(socket.gethostname()) # get ip
PORT = 5050 # the server port
ADDR = (IP, PORT) # addr use for 
#server function

def binding(): #binding function
    server.bind(ADDR) #binding the server
    print("[$] server binded") #announcement

def start():
    try:
        server.listen(5)
        print(f"[$] server listening on {IP}") # start function
    except socket.error as e:
        print("[!] ERROR: {}".format( #if some error happen, do this
            e
            )
        )

def accepting():
    global conn #used for all (sending, receiving and more)
    global addr #used for display
    global conn1 
    global addr1
    client_list = []
    print("[*] waiting for connection....")
    conn, addr = server.accept() #accepting the client 1
    print(f"[$] {addr} has been connected with connection: {conn}")
    conn1, addr1 = server.accept()# accepting the client 2
    print(f"[$] {addr} has been connected with connection: {conn}")
    length = len(client_list) # counting the amount of client
    if length == 2:
        pass

def receiving_hero(recv_addr, send_addr):
    print("waiting for client to select")
    hero = recv_addr.recv(1024) # client choose a hero
    decoded_hero = hero.decode('utf-8') # decoded for display
    print(f"{recv_addr} choose {decoded_hero}") # displaying the client choose
    send_addr.send(hero) #sending the selection

def sendchoose(c1, c2):
    print("waiting for choose")
    choose = c1.recv(1024)
    c2.send(choose)

# the server works start here
binding() 
start()
accepting()
receiving_hero(conn, conn1)
receiving_hero(conn1, conn)
while True:
    sendchoose(conn, conn1)
    sendchoose(conn1, conn)

