class animal:
    def __init__(self):
        print("animal:생성자")
        self.age = 0
        
    def getOld(self):
        self.age += 1
        
    def __del__(self):
        print("animal:소멸자")
        
    
class human(animal):
    def __init__(self):
        print("human:생성자")
        super().__init__()
        self.skill_lang = 0

    def momstouch(self,stroke):
        self.skill_lang += stroke
    
    def __del__(self):
        print("human:소멸자")

if __name__ == '__main__':
    hum = human()
    print("myoop01",hum.skill_lang)
    print("myoop01",hum.age)
    hum.getOld()
    hum.momstouch(1000)
    print("myoop01",hum.age)
    print("myoop01",hum.skill_lang)


    
        

