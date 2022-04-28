class LeeJY:
    def __init__(self):
        self.money = 10
        super().__init__()
        
    def shout(self, angry):
        self.money += angry
        

class KimJE:
    def __init__(self):
        self.cnt_nuclear = 10
    
    def aoji(self):
        self.cnt_nuclear += 1
        

class LeeUC(LeeJY, KimJE):
    def __init__(self):
        super().__init__()
        
student = LeeUC()

print("student money : ", student.money)
print("student nuclear : ", student.cnt_nuclear)
student.shout(1)
student.aoji()
print("student money : ", student.money)
print("student nuclear : ", student.cnt_nuclear)
    