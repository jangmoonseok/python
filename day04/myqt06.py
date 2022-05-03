import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("myqt06.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        # 화면을 보여준다.
        self.pb.clicked.connect(self.myclick)    # 클릭 시 실행할 function
        self.show()

    def lotto(self):
        arr6 = []
        arr45 = list(range(1, 45 + 1))
        for i in range(1000):
            rndIndex = int(random() * 45)
            temp = arr45[0]
            arr45[0] = arr45[rndIndex]
            arr45[rndIndex] = temp
        
        for i in range(6):
            arr6.append(arr45[i])

        self.lbl1.setText(str(arr6[0]))
        self.lbl2.setText(str(arr6[1]))
        self.lbl3.setText(str(arr6[2]))
        self.lbl4.setText(str(arr6[3]))
        self.lbl5.setText(str(arr6[4]))
        self.lbl6.setText(str(arr6[5]))

    def myclick(self):
        self.lotto()
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()