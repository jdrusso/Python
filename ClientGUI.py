import sys
import socket
from PyQt4 import QtGui, QtCore

class CommThread(QtCore.QThread):
    
    data_received = QtCore.pyqtSignal(object)

    def __init__(self, socketConn, outWidget):
        QtCore.QThread.__init__(self)
        self.socketConn = socketConn
        self.outWidget = outWidget
        print 'TCP Thread initialized.'
        
    def run(self):
        while True:
            data = self.socketConn.recv(1024)
            if data:
                print 'Received: '
                print data
                self.data_received.emit(data)

class SerialWindow(QtGui.QWidget):

    def __init__(self):
        super(SerialWindow, self).__init__()

        self.initUI()

    def initUI(self):
    
        self.HOST = '192.168.1.118'
        self.PORT = 50007

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.connected = False

        self.hostEdit = QtGui.QLineEdit()
        self.hostBtn = QtGui.QPushButton("Connect", self)

        self.serialIn = QtGui.QTextEdit()

        self.serialOut = QtGui.QLineEdit()
        self.serialBtn = QtGui.QPushButton("Send", self)

        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)

        self.grid.addWidget(self.hostEdit, 0, 3)
        self.grid.addWidget(self.hostBtn, 0, 4)

        self.grid.addWidget(self.serialIn, 1, 0, 5, 0)

        self.grid.addWidget(self.serialOut, 6, 0)
        self.grid.addWidget(self.serialBtn, 6, 4)

        self.hostBtn.clicked.connect(self.hostConnect)
        self.serialBtn.clicked.connect(self.serialSend)

        self.hostEdit.setText('192.168.1.118')

        self.setLayout(self.grid)

        self.setGeometry(300, 300, 550, 350)
        self.setWindowTitle('Arduino Serial Comms')
        self.show()

    def hostConnect(self):

        HOST = self.hostEdit.text()
        self.s.connect((self.HOST,self.PORT))
        
        self.serialReader = CommThread(self.s, self.serialIn)
        self.serialReader.data_received.connect(self.on_data_received)
        self.serialReader.start()
        
    def on_data_received(self, data):
        self.serialIn.append(data)

    def serialSend(self):
    
        output = str(self.serialOut.text())
        self.s.send(output)
        self.serialIn.setText('')

def main():

    app = QtGui.QApplication(sys.argv)
    mw = SerialWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()