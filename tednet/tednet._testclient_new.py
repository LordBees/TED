import socket
import threading
class socket_io:
    ##client socket object
    socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ##threads need to go here as they are not setup properly in the init loop
    host = ''
    port = ''
    t1 = ''##may work here
    t2 = ''
    globaldata = ''
    def __init__(self,host_ip_name,port_name):
        self.host = host_ip_name
        self.port = port_name
        print(tuple([self.host,self.port]))
        if True:#try:
            self.socket.connect(tuple([self.host,self.port]))#('localhost',9999)
            print('connected to \nport:'+str(self.port)+'\nip:'+str(self.host)+'\n========')
            self.t1 = threading.Thread(target=self.readData)
            self.t1.start()
            print('thread 1 start')
            self.t2 = threading.Thread(target=self.eventloop)
            self.t2.start()
            print('thread 2 start\n')
        if False: #except:
            print('socket error!\nconnection failed to host.\nport: '+str(self.port)+'\nip: '+str(self.host))
            

    def send_data(self,data):
        print('sending: '+data)
        self.socket.send(data.encode('utf-8'))
        print('data_SENT!')

    def heartbeat(self,connected):
        if connected:
            self.socket.send('Heartbeat_ping'.encode('utf-8'))

    def readData(self):
        print('reading')
        while True:
            #print('rdl')
            data = self.socket.recv(1024)
            if data:
                print('Received: ' + data.decode('utf-8'))
                self.globaldata = data.decode('utf-8')



    def eventloop(self):
        while True:
            #self.t1.start()
            self.send_data(input('t@'))
            #self.t1.join()
            self.t1.join()##restart thread as wait4recieve as input halts threads
            self.t1.start()
    
s = socket_io('localhost',9999)
##s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
##s.connect(('localhost',9999))
##globaldata = ''
##
##
##def sendData(data):
##    print('sending: '+data)
##    s.send(data.encode('utf-8'))
##    print('data_SENT!')
##    
##            
###t2 = threading.Thread(target=sendData)
###t2.start()
##
##def heartbeat(connected):
##    if connected:
##        s.send('Heartbeat_ping'.encode('utf-8'))
##
##
##
##def readData():
##    global globaldata
##    print('reading')
##    while True:
##        #print('rdl')
##        data = s.recv(1024)
##        if data:
##            print('Received: ' + data.decode('utf-8'))
##            globaldata = data.decode('utf-8')
##            
##            
##
##t1 = threading.Thread(target=readData)
##t1.start()
##
##
##
##def eventloop():
##    while True:
##        sendData(input('t@'))
##    
##t2 = threading.Thread(target=eventloop)
##t2.start()
##
##
####def readData():
####    print('reading')
####    while True:
####        print('rdl')
####        data = s.recv(1024)
####        if data:
####            print('Received: ' + data.decode('utf-8'))
####
####t1 = threading.Thread(target=readData)
####t1.start()
####
####def sendData(data):
####    print('sending')
####    watcher = 0
####    while True:
####        if watcher >= 10:
####            #heartbeat('True')
####            print('sndl')
####            intxt = input('>')
####            #print(intxt)
####            s.send(intxt.encode('utf-8'))
####            print('data_SENT!')
####            #print(intxt)
####            heartbeat('True')
####            watcher=0
####            
####        else:
####            watcher+=1
####            print (watcher)
####            
####t2 = threading.Thread(target=sendData)
####t2.start()
