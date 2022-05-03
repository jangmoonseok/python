import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from random import random
from PyQt5.QtCore import Qt

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("myqtA.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.com = []
        self.mine = []
        self.result = ""
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        # 화면을 보여준다.
        self.pb.clicked.connect(self.myclick) 
        self.comAnswer()   # 클릭 시 실행할 function
        self.show()
    
    def comAnswer(self):
        arr9 = list(range(1,9 + 1))
        for i in range(100):
            rnd = int(random() * 9)
            temp = arr9[0]
            arr9[0] = arr9[rnd]
            arr9[rnd] = temp
        
        for i in arr9[0:3]:
            self.com.append(i)

    def check(self):
        strike = 0;
        ball = 0;
        for i in range(len(self.com)):
            for j in range(len(self.mine)):
                if self.com[i] == self.mine[j] and i == j:
                    strike += 1
                elif self.com[i] == self.mine[j] and i != j:
                    ball += 1
                else:
                    pass
        result = "{} -> {}S {}B\n".format(self.le.text(), str(strike), str(ball))
        self.result += result
        if strike == 3:
            QMessageBox.information(self, "알림말","정답입니다!")
        
        
    
    def myclick(self):
        mine = self.le.text()
        for i in mine:
            self.mine.append(int(i))
        self.check()
        self.te.setText(self.result)
        self.mine = []
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()