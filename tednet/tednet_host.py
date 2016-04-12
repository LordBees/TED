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
        #self.senddata(self.data)##test sendback
        self.handledata(self.data)##echo back data
        self.data = ''##clear buffer
        
    def senddata(self,indata,manual = False):
        print('datasending')
        if True:
            if manual == True:
                self.request.sendall(str(input(';')).encode('utf-8'))
            else:
                self.request.sendall(str(indata).encode('UTF-8'))
                print('sent'+str(indata))
        
    def handledata(self,data):##catch disconnects need to
        print('handling')
        dattemp = ''
        for x in range(0,len(data)):
            print(str(chr(data[x])))
            dattemp = dattemp + str(chr(data[x]))##bytes2chr or something?
        print (dattemp)
        if 'Heartbeat_' in dattemp:
            self.senddata('Heartbeat_pong')
        else:
            self.senddata(dattemp)

        if dattemp[0] == '@':
            dattemp = dattemp.strip('@')##strips command
            print('command')
            pdat = dattemp.split(' ')
            print(pdat)
            if 'test' in pdat:
                print('test in string')
            
        print('handled!')
        

server = socketserver.TCPServer(('localhost', 9999), MyTCPHandler)
server.serve_forever()
