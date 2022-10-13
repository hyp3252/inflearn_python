

for i in range(5):
    print("안녕하세요")
    
    
sum = 0
for i in range(10):
    sum += i
    
print("0~9까지의 합 :", sum)


sum = 0
for i in range(0,10):
    sum += i
print("0~9까지의 합 :", sum)


sum = 0
for i in range(0,10,2):
    sum += i
    print("짝수 누계 출력 :", sum)
print("0~9까지의 짝수의 합 :", sum)
