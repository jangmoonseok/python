import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
from PyQt5.QtCore import Qt

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("myqt09.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.com = ""
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        # 화면을 보여준다.
        self.pb.clicked.connect(self.myclick)    # 클릭 시 실행할 function
        self.leMine.returnPressed.connect(self.myclick)
        self.show()
    
    def comAnswer(self):
        rnd = int(random() * 3)
        if rnd == 0:
            self.com = "가위"
        elif rnd == 1:
            self.com = "바위"
        else:
            self.com = "보"
            
    # def keyPressEvent(self, e):
    #     if e.key() == 16777220:
    #         self.myclick()
    
    def myclick(self):
        self.comAnswer()
        mine = self.leMine.text()
        result = ""
        if self.com == "가위":
            if mine == "가위":
                result = "비겼습니다."
            elif mine == "바위":
                result = "이겼습니다."
            else:
                result = "졌습니다."
        elif self.com == "바위":
            if mine == "가위":
                result = "졌습니다."
            elif mine == "바위":
                result = "비겼습니다."
            else:
                result = "이겼습니다."
        else:
            if mine == "가위":
                result = "이겼습니다."
            elif mine == "바위":
                result = "졌습니다."
            else:
                result = "비겼습니다."
        self.leCom.setText(self.com)
        self.leResult.setText(result)
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()