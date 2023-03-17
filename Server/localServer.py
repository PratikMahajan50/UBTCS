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
    global paths,server_socket,port,db,active,complete
    print("Initializing Server")
    #Demo data, will be updated by database
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
    paths = db["Paths"]

def client(addr,client_socket):
    global ActiveIds
    #Accept the camera name
    cname = client_socket.recv(1024).decode()
    print("Starting session for Camera: ",cname)

    #Start Receiving numbers
    while(True):
        number = client_socket.recv(1024).decode()
        print(number)
        res = list(active.find({"ID":number}))

        if len(res):
            #check if path exists by finding the associated weight of the source and destinaion
            src="C1"
            des="C2"
            w = paths.find({"src":src,"des":des})
            if len(w):
                print("Error")
            else:
                print("Complete")
                complete.insert_one({"ID":number,"src":cname,"des":des})
                #Transaction complete
            
        else:
            print("Inserting records")
            active.insert_one({"ID":number,"src":cname})


i=0
initServer()
while i<nodes.__len__()-3:
    client_socket,addr = server_socket.accept()
    thread = threading.Thread(target=client, args=(addr,client_socket))
    thread.start()
    print("connected Cameras: ",threading.activeCount()-1)
    i+=1

