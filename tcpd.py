import socket,select

from PySide6 import QtCore

class MyTCPserver(QtCore.QObject):

    client_signal = QtCore.Signal(tuple)
    data_signal = QtCore.Signal(bytes)

    def __init__(self):
        super().__init__()
        self.local_port = 9980
        self.run_flag = False

    def set_local_port(self,port):
        self.local_port = port

    def start_server(self):
        self.run_flag = True
        self.myserver = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.myserver.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        #self.myserver.setblocking(False)
        self.myserver.bind(('0.0.0.0',self.local_port))
        self.myserver.listen(1)
        self.inputs = [self.myserver]
        while self.run_flag is True:
            readable, writable, exceptional = select.select(self.inputs, [], [], 0.5)
            for c in readable:
                if c is self.myserver:
                    self.connection, self.client_address = c.accept()
                    self.client_signal.emit(self.client_address)
                    self.inputs.append(self.connection)
                else:
                    data = c.recv(1024)
                    if data:
                        print(type(data))
                        self.data_signal.emit(data)
                    else:
                        self.inputs.remove(c)
                        c.close()

    def stop_server(self):
        self.run_flag = False
        tmp_list = list(self.inputs)
        self.inputs.clear()
        for c in tmp_list:
            c.close()

#Test
if __name__ == "__main__":

    MyServer = MyTCPserver()
    MyServer.start_server()
