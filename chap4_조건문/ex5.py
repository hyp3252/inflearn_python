# 정수입력 받은 숫자 중 둘 중에서 가장 큰 수



a = int(input("첫번째 정수 입력 :"))
b = int(input("첫번째 정수 입력 :"))
maximum = 0
if a>b:
    maximum = a
elif a==b:
    print("a와 b는 같음")
else:
    maximum = b
    
print("둘 중 큰 수",maximum)