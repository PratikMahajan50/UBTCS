# this is a localserver program 


def initServer():
    #Accept Nodes
    #Accept Paths and associted weights
    global paths,nodes
    i=int(input("Enter Number of Nodes: "))
    paths = [[{"src":"x"},{"des":"y"},{"w":0}]]
    nodes = []
    while i:
        nodes.append(input("Enter Node Name: "))
        i-=1
initServer()