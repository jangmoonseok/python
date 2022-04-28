# 출력하고싶은 단수를 입력하세요 >> 6 Enter
# 6 * 1 = 6
# 6 * 2 = 12 ...

arr = range(1,10)
dan = input("출력하고싶은 단수를 입력하세요")
idan = int(dan)

for i in arr:
    print("{} * {} = {}".format(dan,i,idan * i))