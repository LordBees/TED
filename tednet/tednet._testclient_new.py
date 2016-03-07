import socket
import threading

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost',9999))
globaldata = ''


def sendData(data):
    print('sending: '+data)
    s.send(data.encode('utf-8'))
    print('data_SENT!')
    
            
#t2 = threading.Thread(target=sendData)
#t2.start()

def heartbeat(connected):
    if connected:
        s.send('Heartbeat_ping'.encode('utf-8'))



def readData():
    global globaldata
    print('reading')
    while True:
        #print('rdl')
        data = s.recv(1024)
        if data:
            print('Received: ' + data.decode('utf-8'))
            globaldata = data.decode('utf-8')
            
            

t1 = threading.Thread(target=readData)
t1.start()



def eventloop():
    while True:
        sendData(input('t@'))
    
t2 = threading.Thread(target=eventloop)
t2.start()


##def readData():
##    print('reading')
##    while True:
##        print('rdl')
##        data = s.recv(1024)
##        if data:
##            print('Received: ' + data.decode('utf-8'))
##
##t1 = threading.Thread(target=readData)
##t1.start()
##
##def sendData(data):
##    print('sending')
##    watcher = 0
##    while True:
##        if watcher >= 10:
##            #heartbeat('True')
##            print('sndl')
##            intxt = input('>')
##            #print(intxt)
##            s.send(intxt.encode('utf-8'))
##            print('data_SENT!')
##            #print(intxt)
##            heartbeat('True')
##            watcher=0
##            
##        else:
##            watcher+=1
##            print (watcher)
##            
##t2 = threading.Thread(target=sendData)
##t2.start()
