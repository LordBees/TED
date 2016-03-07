import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
       while True:
        self.data = self.request.recv(1024)
        if not self.data:
            print('DISCONNECTED')
            break
        print('RECEIVED: ' + str(self.data))
        #self.request.sendall(str(self.data)[::-1].encode('utf-8'))
        self.senddata(self.data)
        #self.handledata(self.data)
        
    def senddata(self,indata):
        print('datasending')
        while True:
            self.request.sendall(str(input(';')).encode('utf-8'))
        
    def handledata(self,data):
        print('handling')
        dattemp = ''
        for x in range(0,len(data)):
            print(str(chr(data[x])))
            dattemp = dattemp + str(chr(data[x]))
        print (dattemp)
        if 'Heartbeat_' in dattemp:
            self.senddata('Heartbeat_pong')
        else:
            self.senddata(dattemp)
            
        print('handled!')
        

server = socketserver.TCPServer(('localhost', 9999), MyTCPHandler)
server.serve_forever()
