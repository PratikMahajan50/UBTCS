# this is a localserver program 
import socket,cv2,pickle,struct,time
import threading,os
import numpy as np
import pymongo
#TEMP DATA
ActiveIds = []


def initServer():
    #Accept Nodes
    #Accept Paths and associted weights
    global paths,nodes,server_socket,port,db,active,complete
    print("Initializing Server")
    #Demo data, will be updated by database
    nodes = ["C1","C2","C3","C4"]
    paths = [
                [{"src":"C1"},{"des":"C2"},{"w":10}],
                [{"src":"C2"},{"des":"C1"},{"w":10}],
                
                [{"src":"C1"},{"des":"C3"},{"w":20}],
                [{"src":"C3"},{"des":"C1"},{"w":20}],
                
                [{"src":"C1"},{"des":"C4"},{"w":30}],
                [{"src":"C4"},{"des":"C1"},{"w":30}],
                
                [{"src":"C2"},{"des":"C3"},{"w":10}],
                [{"src":"C3"},{"des":"C2"},{"w":10}],
                
                [{"src":"C2"},{"des":"C4"},{"w":20}],
                [{"src":"C4"},{"des":"C2"},{"w":20}],
                
                [{"src":"C3"},{"des":"C4"},{"w":10}],
                [{"src":"C4"},{"des":"C3"},{"w":10}],
             ]
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 8081
    socket_address = (input("Enter Server IP: "),port)
    server_socket.bind(socket_address)
    server_socket.listen()
    print("Listening at ",socket_address)
    print("Initializing Database")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["ubtcs"]
    active = db["ActiveRecords"]
    complete = db["CompletedRecords"]


def client(addr,client_socket):
    global ActiveIds
    #Accept the camera name
    cname = client_socket.recv(1024).decode()
    print("Starting session for Camera: ",cname)

    #Start Receiving numbers
    while(True):
        number = client_socket.recv(1024).decode()
        if active.find({"ID":number}):
            pass
        else:
            print("Inserting records")
            active.insert({"ID":number,"src":cname})


i=0
initServer()
while i<nodes.__len__()-3:
    client_socket,addr = server_socket.accept()
    thread = threading.Thread(target=client, args=(addr,client_socket))
    thread.start()
    print("connected Cameras: ",threading.activeCount()-1)
    i+=1

