import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("myqt04.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        # 화면을 보여준다.
        self.pb.clicked.connect(self.myclick)    # 클릭 시 실행할 function
        self.show()
    
    def comAnswer(self):
        rnd = int(random() * 2)
        if rnd == 1:
            self.le_com.setText("홀")
        else:
            self.le_com.setText("짝")
    
    def myclick(self):
        self.comAnswer()
        mine = self.le_mine.text()
        if mine == self.le_com.text():
            self.le_result.setText("이겼습니다.")
        else:
            self.le_result.setText("졌습니다.")
            
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()