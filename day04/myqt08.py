import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("myqt08.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        self.w = QWidget()                                    # The QWidget widget is the base class
        self.w.setWindowTitle('Calling')
        self.w.resize(400, 200)
        self.str = ""
        # 화면을 보여준다.
        self.pb1.clicked.connect(self.myclick)    # 클릭 시 실행할 function
        self.pb2.clicked.connect(self.myclick)    # 클릭 시 실행할 function
        self.pb3.clicked.connect(self.myclick)    # 클릭 시 실행할 function
        self.pb4.clicked.connect(self.myclick)    # 클릭 시 실행할 function
        self.pb5.clicked.connect(self.myclick)    # 클릭 시 실행할 function
        self.pb6.clicked.connect(self.myclick)    # 클릭 시 실행할 function
        self.pb7.clicked.connect(self.myclick)    # 클릭 시 실행할 function
        self.pb8.clicked.connect(self.myclick)    # 클릭 시 실행할 function
        self.pb9.clicked.connect(self.myclick)    # 클릭 시 실행할 function
        self.pb0.clicked.connect(self.myclick)    # 클릭 시 실행할 function
        self.pbCall.clicked.connect(self.call)    # 클릭 시 실행할 function
        self.show()

    
    def myclick(self):
        sender = self.sender();
        self.str += sender.text()
        self.le.setText(self.str)
        
    def call(self):
        QMessageBox.information(self.w, "Calling", self.le.text() + " calling...")
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()