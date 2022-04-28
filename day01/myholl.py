import random

my = input("홀/짝을 입력하세요")
com = random.random()

if com > 0.5:
    com = "홀"
else:
    com = "짝"

if my == com:
    print("com",com)
    print("my",my)
    print("이겼습니다.")
else:
    print("com", com)
    print("my", my)
    print("졌습니다")