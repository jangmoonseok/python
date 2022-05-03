import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("myqt05.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        # 화면을 보여준다.
        self.pb.clicked.connect(self.myclick)    # 클릭 시 실행할 function
        self.show()
        

    def printDan(self):
        dan = self.le.text()
        idan = int(dan)
        result = ""
        result += dan + " * " + str(1) + " = " + str(idan * 1) + "\n"
        result += dan + " * " + str(2) + " = " + str(idan * 2) + "\n"
        result += dan + " * " + str(3) + " = " + str(idan * 3) + "\n"
        result += dan + " * " + str(4) + " = " + str(idan * 4) + "\n"
        result += dan + " * " + str(5) + " = " + str(idan * 5) + "\n"
        result += dan + " * " + str(6) + " = " + str(idan * 6) + "\n"
        result += dan + " * " + str(7) + " = " + str(idan * 7) + "\n"
        result += dan + " * " + str(8) + " = " + str(idan * 8) + "\n"
        result += dan + " * " + str(9) + " = " + str(idan * 9)
        self.te.setText(result)

    def myclick(self):
        self.printDan()
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()