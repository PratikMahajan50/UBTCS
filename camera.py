# This is the first comment 

#Importing required packages
import cv2,pickle, socket, struct

#Starting the video capturing
cap = cv2.VideoCapture(0)   #considering only 1 camera is connected to the hardware
print("Video Capture Complete")

#Configuring the network
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect((input("Enter the Server IP: "),8080))

#Starting the streaming and sending the numberplate number to the server

if clientSocket:
    while(cap.isOpened()):
        try:
            img,frame = cap.read()
        
        except:
            cap.release()
            print("Video Finished")




