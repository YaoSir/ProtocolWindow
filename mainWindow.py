import sys,threading,datetime

from PySide6.QtWidgets import QApplication, QWidget

from protocolWindow import Ui_Form
from tcpd import MyTCPserver
 

def run_server(server):
    server.start_server()

class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.my_server = MyTCPserver()
        self.ui.setupUi(self,self.my_server)

    def slot_set_port(self,str):
        port = int(str)
        self.my_server.set_local_port(port)

    def solt_server_state(self,flag):
        if flag == True:
            self.backThread = threading.Thread(target=run_server,daemon=True,args=(self.my_server,))
            self.backThread.start()
        else:
            self.my_server.stop_server()

    def show_client_info(self,info):
        self.ui.label_3.setText(info[0])
        self.ui.label_3.show()
        self.ui.label_5.setText(str(info[1]))
        self.ui.label_5.show()

    def show_client_data(self,data):
        self.ui.textBrowser.ensureCursorVisible()
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        self.ui.textBrowser.append("<font size=2 color=\"#47E26B\">"+"<i>" + current_time + "<i>" + "</font>")
        self.ui.textBrowser.append(bytes.decode(data)+'\n')


if __name__ == "__main__":
    app = QApplication(sys.argv)
 
    window = mainWindow()
    window.show()

    sys.exit(app.exec())