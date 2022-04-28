# 1~9까지의 수 중에서 3가지를 랜덤으로 중복없이 출력하시오
from random import random

# 방법1)
# arr = []
#
# arr.append(int(random() * 9 + 1))
# while len(arr) < 3:
#     rnd = int(random() * 9 + 1)
#     if rnd not in arr:
#         arr.append(rnd)
#
# print(arr)
    
arr9 = [1,2,3,4,5,6,7,8,9]


for i in range(100):
    rnd = int(random() * 9)
    temp = arr9[0]
    arr9[0] = arr9[rnd]
    arr9[rnd] = temp

# print(arr9[0],arr9[1],arr9[2])
print(arr9[0:3])

    