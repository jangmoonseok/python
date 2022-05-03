import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel,\
    QFormLayout, QPushButton, QGridLayout

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("my5mok01.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        self.setGeometry(700, 300, 760, 760)
        self.omokPan()
        # 화면을 보여준다.
        self.show()
    
    def omokPan(self):  
        layout = QGridLayout()
        label = QLabel()
        label.resize(40,40)
        label.setStyleSheet("background-image:url(0.png)")
        layout.addWidget(label,0,0)

        self.centralwidget.setLayout(layout)
            
                    
            
 
 
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()