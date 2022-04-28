# 1~45까지 수 중에서 6가지 숫자를 중복없이 랜덤으로 출력하시오

from random import random

# arr = []
#
# arr.append(int(random() * 45 + 1))
# while len(arr) < 6:
#     rnd = int(random() * 45 + 1)
#     if rnd not in arr:
#         arr.append(rnd)
#
# print(arr)

arr45 = list(range(1, 45+1))
arr6 = []

while True:
    rnd = int(random() * 45)
    if arr45[rnd] == -1:
        pass
    else:
        arr6.append(arr45[rnd])
        arr45[rnd] = -1
        
    if len(arr6) >= 6:
        break
print(arr6)
    


