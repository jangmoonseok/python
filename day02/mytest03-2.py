# 1~9까지의 수 중에서 3가지를 랜덤으로 중복없이 출력하시오
from random import random
    
arr9 = [1,2,3,4,5,6,7,8,9]
arr3 = []

while True:
    rnd = int(random() * 9)
    if arr9[rnd] == -1:
        pass
    else:
        arr3.append(arr9[rnd])
        arr9[rnd] = -1
        
    if len(arr3) >= 3:
        break
print(arr3)


    