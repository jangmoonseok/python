import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel,\
    QFormLayout, QPushButton, QGridLayout, QMessageBox
from PyQt5.Qt import QSize, QEvent
from networkx.generators import line
from conda.common._logic import TRUE



# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("my5mok03_19.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        self.flag_wb = True;
        self.flag_over = False;
        self.arr2d = [
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
        ]
        self.pb2d = []
        for i in range(19):
            line = [] 
            for j in range(19):            
                obj = QPushButton(self)
                obj.setIcon(QtGui.QIcon('0.png'))
                obj.setIconSize(QSize(40,40))
                obj.setGeometry(0 + (40 * j),0 + (40 * i),40,40)
                obj.setToolTip("{},{}".format(j, i))
                obj.clicked.connect(self.myclick)
                line.append(obj)
            self.pb2d.append(line)
       
        self.setGeometry(700, 300, 900, 900)
        self.pb.clicked.connect(self.myreset)
        self.myrender()
        self.show()
    
    
        
    def myclick(self):
        if self.flag_over:
            return 
        
        sender = self.sender()
        xyArr =  sender.toolTip().split(',')
        x = int(xyArr[0])
        y = int(xyArr[1])
        if self.arr2d[y][x] != 0:
            return
        stone = -1
        if self.flag_wb:
            self.arr2d[y][x] = 1
            stone = 1
        else:
            self.arr2d[y][x] = 2
            stone = 2
                
        up = self.checkUp(x,y,stone)
        dw = self.checkDW(x, y, stone)
        ri = self.checkRI(x, y, stone)
        le = self.checkLE(x, y, stone)
        ul = self.checkUL(x, y, stone)
        ur = self.checkUR(x, y, stone)
        dl = self.checkDL(x, y, stone)
        dr = self.checkDR(x, y, stone)
        
        
        d1 = up + dw + 1
        d2 = le + ri + 1
        d3 = ul + dr + 1
        d4 = ur + dl + 1
        
            
        self.myrender()
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5:
            self.flag_over = True
            if self.flag_wb:
                QMessageBox.information(self, "결과", "게임종료 : 백돌승리!")
            else:
                QMessageBox.information(self, "결과", "게임종료 : 흑돌승리!")

                    
        self.flag_wb = not self.flag_wb
    
    def checkUp(self,x,y,stone):    
        cnt = 0
        
        try:  
            while True:
                y -= 1
                if x < 0:
                    return cnt
                if y < 0:
                    return cnt
                
                if self.arr2d[y][x] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
            
    def checkDW(self,x,y,stone):    
        cnt = 0

        try:  
            while True:
                y += 1
                if x < 0:
                    return cnt
                if y < 0:
                    return cnt
                if self.arr2d[y][x] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt

    def checkRI(self,x,y,stone):    
        cnt = 0

        try:  
            while True:
                x += 1
                if x < 0:
                    return cnt
                if y < 0:
                    return cnt
                if self.arr2d[y][x] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkLE(self,x,y,stone):    
        cnt = 0

        try:  
            while True:
                x -= 1
                if x < 0:
                    return cnt
                if y < 0:
                    return cnt
                if self.arr2d[y][x] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkUL(self,x,y,stone):    
        cnt = 0

        try:  
            while True:
                x -= 1
                y -= 1
                if x < 0:
                    return cnt
                if y < 0:
                    return cnt
                if self.arr2d[y][x] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkUR(self,x,y,stone):    
        cnt = 0

        try:  
            while True:
                x += 1
                y -= 1
                if x < 0:
                    return cnt
                if y < 0:
                    return cnt
                if self.arr2d[y][x] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkDL(self,x,y,stone):    
        cnt = 0

        try:  
            while True:
                x -= 1
                y += 1
                if x < 0:
                    return cnt
                if y < 0:
                    return cnt
                if self.arr2d[y][x] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkDR(self,x,y,stone):    
        cnt = 0

        try:  
            while True:
                x += 1
                y += 1
                if x < 0:
                    return cnt
                if y < 0:
                    return cnt
                if self.arr2d[y][x] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def myrender(self):
        for i in range(len(self.arr2d)):
            for j in range(len(self.arr2d[i])):
                if self.arr2d[i][j] == 0:
                    self.pb2d[i][j].setIcon(QtGui.QIcon('0.png'))
                elif self.arr2d[i][j] == 1:
                    self.pb2d[i][j].setIcon(QtGui.QIcon('1.png'))
                else:
                    self.pb2d[i][j].setIcon(QtGui.QIcon('2.png'))
                    
                    
    
    def myreset(self):
        for i in range(len(self.arr2d)):
            for j in range(len(self.arr2d[i])):
                    self.arr2d[i][j] = 0
        self.myrender()
        self.flag_over = False
        self.flag_wb = True


            
            
 
 
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()