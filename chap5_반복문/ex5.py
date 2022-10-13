# 피보나치 수열
# F(n+2) = F(n+1) + F(n)


num1 = 0
num2 = 1
fib = int(input("정수입력 : "))
for i in range(fib+1):
    num1, num2 = num2, num1 + num2
    print(num1)
