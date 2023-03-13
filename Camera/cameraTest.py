#Python file with demo data for testing the functionalities
# This is the first comment 

#Importing required packages
import numpy as np
import cv2,pickle, socket, struct,imutils,easyocr

#Starting the video capturing
#cap = cv2.VideoCapture(0)   #considering only 1 camera is connected to the hardware
i=1
print("Video Capture Complete")

#Configuring the network
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#clientSocket.connect((input("Enter the Server IP: "),8080))

#Starting the streaming and sending the numberplate number to the server

if True:
    while(i<120):
            #ret,frame = cap.read()

            fname = "Samples\S (" + str(i)+ ").jpg"
            frame = cv2.imread(fname)
            
            #Adding the AI logic
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(frame,ksize=(7,7),sigmaX=0)
            edge = cv2.Canny(blur,90,200)
            edge = cv2.dilate(edge,kernel=(3,3),iterations=2)

            keypoints = cv2.findContours(edge.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(keypoints)
            contours = sorted(contours,key = cv2.contourArea,reverse=True)[:10]#first top ten contours
            list = []
           
            for c in contours:
                length = cv2.arcLength(c,True)
                approx = cv2.approxPolyDP(c,0.05*length,True)
                #high the number then most rough the estimation
                if (len(approx)==4):
                    list = approx
                    break

            mask = np.zeros_like(frame)
            new_cont = cv2.drawContours(mask,[list],0,255,-1)
            masked = cv2.bitwise_and(frame,frame,mask =mask)
            (x,y) = np.where(mask==255)
            (x1,y1) = (np.min(x),np.min(y))
            (x2,y2) = (np.max(x),np.max(y))
            final = masked[x1:x2+1,y1:y2+1]
            final = cv2.cvtColor(final,cv2.COLOR_BGR2RGB)
            reader = easyocr.Reader(['en'])
            result = reader.readtext(final)   
            text = result[1][1]
            
            print(text)       
            i+=1  
        




