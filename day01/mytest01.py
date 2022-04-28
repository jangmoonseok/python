# 앞 수를 넣으세요 1 Enter
# 끝 수를 넣으세요 10 Enter
# 당신의 수의 합은 55입니다.

a = input("앞 수를 넣으세요")
b = input("끝 수를 넣으세요")

arr = range(int(a),int(b) + 1)
sum = 0
for i in arr:
    sum += i

print("당신의 수의 합은",sum ,"입니다")