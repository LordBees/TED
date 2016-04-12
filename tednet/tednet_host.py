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
                self.request.sendall(str(input(';: ')).encode('utf-8'))
            else:
                self.request.sendall(str(indata).encode('UTF-8'))
                print('sent'+str(indata))##dbg
        
    def handledata(self,data):##catch disconnects need to
        print('handling')
        dattemp = ''
        for x in range(0,len(data)):
            print(str(chr(data[x])))##dbg
            dattemp = dattemp + str(chr(data[x]))##bytes2chr or something?
        print (dattemp)##dbg
        if 'Heartbeat_' in dattemp:
            self.senddata('Heartbeat_pong')
        else:
            self.senddata(dattemp)

        if dattemp[0] == '@':
            ##dattemp = dattemp.strip('@')##strips command##n/a because @ needed to define cmds
            print('command')
            pdat = dattemp.split(' ')##splits on spaces
            print(pdat)
            cmd_iter_flag = False##for skipping other commands on each cycle on the same iteration
            cmd_dat_flag = 0##for flagging data on each iteration no of loops to skip inc current oneso 1 ignore would be 2 as it includes the loop remainder
            for x in pdat:
                
                cmd_iter_flag = False
                print(cmd_dat_flag)
                #cmd_dat_flag = 0#False
                ##if for flag here instead? -Note wont work as iteration will still select regardless but only will count on next loop
                if cmd_dat_flag >0:
                    cmd_dat_flag += -1
                if x == '@test'and not cmd_iter_flag:
                    cmd_iter_flag = True
                    print('test in string')
                    
                if x == '@print'and not cmd_iter_flag:##if '@print' in pdat:
                    cmd_iter_flag = True
                    cmd_dat_flag = 2#no of loops to avoid
                    print('printing: '+pdat[pdat.index('@print')+1])##pdat may need to be changed here to fit iteration
                    
                if not cmd_iter_flag and cmd_dat_flag == 0:
                    print('command segment" '+str(x)+' " is invalid!')
                    
                #cmd_dat_flag = False##is here so cleared at iteration END
            
        print('handled!')
        

server = socketserver.TCPServer(('localhost', 9999), MyTCPHandler)
server.serve_forever()
