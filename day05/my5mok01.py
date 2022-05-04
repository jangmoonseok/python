import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel,\
    QFormLayout, QPushButton, QGridLayout
from PyQt5.Qt import QSize


# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("my5mok01.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        self.flag = 0;
        for i in range(10): 
            for j in range(10):            
                obj = QPushButton(self)
                obj.setIcon(QtGui.QIcon('0.png'))
                obj.setIconSize(QSize(40,40))
                obj.setGeometry(0 + (40 * j),0 + (40 * i),40,40)
                obj.clicked.connect(self.myclick)
       
        self.setGeometry(700, 300, 760, 760)
        self.pb.clicked.connect(self.myreset)
        self.show()
    
    
        
    def myclick(self):
        sender = self.sender()
        if self.flag == 1:
            self.black(sender)
            self.flag = 0
        else:
            self.white(sender)
            self.flag = 1
        
    
    def myreset(self):
        QPushButton().setIcon(QtGui.QIcon('0.png'))
            
    def black(self, sender):
        sender.setIcon(QtGui.QIcon("2.png"))
    def white(self, sender):            
        sender.setIcon(QtGui.QIcon("1.png"))
            
 
 
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()