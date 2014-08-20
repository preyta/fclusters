import sys
from PyQt4 import QtGui, QtCore

class MyWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.resize(250, 150)
        self.center()
        self.setWindowTitle('ICON')
        self.setWindowIcon(QtGui.QIcon('E:\nstl\fcluster\img\Icon.png'))
    def center(self):
        screen=QtGui.QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
        
app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
sys.exit(app.exec_())



