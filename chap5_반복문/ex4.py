# for 문을 이용하여 팩토리얼을 계산하는 프로그램 작성


fac_num = int(input("정수를 입력하세요"))
factorial = 1

for i in range(1, fac_num+1):
    factorial *= i
    
print(factorial)