# 사용자로부터 2개의 정수값을 입력받고 첫번째 입력받은 값부터 두번째 입력값까지의 범위내에서 3의 배수이면서 4의 배수를 제외하고 출력


a = int(input("첫번째 정수: "))
b = int(input("두번째 정수: "))

for i in range(a, b+1):
    if i%3 != 0 and i%4 != 0:
        print(i)
# 혹은

# for i in range(a,b+1):
#     if i%3 == 0 and i%4 == 0:
#         continue
    
#     print(i)