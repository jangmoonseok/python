# 첫 수를 넣으세요 >> 1 Enter
# 끝 수를 넣으세요 >> 5 Enter
# 배수를 넣으세요 >> 2 Enter
# 1에서 부터 5까지의 2의 배수의 합은 6입니다.

a = int(input("첫 수를 넣으세요"))
b = int(input("끝 수를 넣으세요"))
c = int(input("배수를 넣으세요"))

sum = 0

for i in range(a,b+1):
    if i % c == 0: 
        sum += i
        
print("{}에서 부터 {}까지의 {}의 배수의 합은 {}입니다.".format(a, b, c, sum))


