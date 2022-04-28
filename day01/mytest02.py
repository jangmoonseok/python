# 가위/바위/보를 선택하세요 >> 가위 Enter
# 나 : 가위, 컴퓨터 : 바위 >> 결과 : 졌습니다.
import random

com = random.randrange(0,3)
my = input("가위/바위/보를 입력하세요")
result = ""

if com == 0:
    com = "가위"
elif com == 1:
    com = "바위"
else:
    com = "보"

if my == "가위":
    if com == "가위":
        result = "비겼습니다"
    elif com == "바위":
        result = "졌습니다"
    else:
        result = "이겼습니다"
elif my == "바위":
    if com == "가위":
        result = "이겼습니다"
    elif com == "바위":
        result = "비겼습니다"
    else:
        result = "졌습니다"
else:
    if com == "가위":
        result = "졌습니다"
    elif com == "바위":
        result = "이겼습니다"
    else:
        result = "비겼습니다"

print("나:", my)
print("컴퓨터:", com)
print("결과:",result)