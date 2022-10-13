# 사용자로부터 상품금액을 입력받아 상품의 총 가격을 계산
# 사용자가 몇 개의 상품을 구매할지 모르니까 무한루프를 이용하고 사용자가 끝이라고 입력하면 루프 탈출
from operator import eq

total = 0
price = ""

while True:
    price = input("상품금액입력. (끝을 입력하면 종료됨) : ")
    if eq(price, "끝"): # eq함수를 이용하여 price=="끝"
        print("상품의 총 가격 : ", total,"원")
        break
    
    else:
        total += int(price)