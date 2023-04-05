# this is a localserver program 
import socket,cv2,pickle,struct,time
import threading,os
import numpy as np
import pymongo
#TEMP DATA
nodes=2


def initServer():
    #Accept Nodes
    #Accept Paths and associted weights
    global paths,server_socket,port,db,active,complete,vehicle
    print("Initializing Server")
    #Demo data, will be updated by database
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 8081
    socket_address = (input("Enter Server IP: "),port)
    server_socket.bind(socket_address)
    server_socket.listen()
    print("Listening at ",socket_address)
    print("Initializing Database")
    localClient= pymongo.MongoClient("mongodb://localhost:27017")
    db = localClient["ubtcs"] 
    active = db["ActiveRecords"]
    paths = db["Paths"]
    print("Server Initialization Completed")
    #Adding remote server mongoDB
    serverIP = input("Enter MongoDBServer IP: ")
    serverClient = pymongo.MongoClient("mongodb://u1:u1@"+serverIP+"/ubtcs")
    db2 = serverClient["ubtcs"] 
    complete = db2["CompletedRecords"]
    vehicle = db2["VehicleDetails"]

#fare per km
def getFare(classDetail):
    map = {
        1:0,   2:2, 3:2, 4:3, 5:3,
        6:3.5, 7:4, 8:5, 9:5, 10:5,
        11:6, 12:6, 13:6, 14:6, 15:7,
        16:7, 17:7, 18:7, 19:7, 20:7  
    }
    return map.get(classDetail)

def client(addr,client_socket):
    global ActiveIds
    #Accept the camera name
    cname = client_socket.recv(1024).decode()
    print("Starting session for Camera: ",cname)

    #Start Receiving numbers
    while(True):
        number = client_socket.recv(1024).decode()
        if not number:
            break
        print(number)
        res = list(active.find({"ID":number}))
        if len(res):
            #check if path exists by finding the associated weight of the source and destinaion
            src=res[0].get("src")
            des=cname
            w = list(paths.find({"src":src,"des":des}))
            if len(w):
                print("Complete")
                complete.insert_one({"ID":number,"src":src,"des":des})
            else:
                print("Error")
            
        else:
            #Fetch the details of the vehicles from local repo if not found go to main repository
            vd = list(vehicle.find({"ID":number}))
            if(len(vd)):
                if(vd[0].get("MVC")=="1"):
                    print("No Toll")
                else:
                    print("Inserting records")
                    f=getFare(vd[0].get("MVC"))
                    active.insert_one({"ID":number,"src":cname,"fare":f})
                
i=0
initServer()
while i<nodes:
    client_socket,addr = server_socket.accept()
    thread = threading.Thread(target=client, args=(addr,client_socket))
    thread.start()
    print("connected Cameras: ",threading.activeCount()-1)
    i+=1
