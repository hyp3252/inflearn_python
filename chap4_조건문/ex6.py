# 물건 구매 시 50000원 이상이면 5%할인, 구입금액을 입력받고 할인금액과 지불금액을 출력


price = int(input("구입금액 :"))
discount = 0

if price >= 50000:
    discount = price * 0.05
    print("물건가격 :", price)
    print("할인금액 :", discount)
    print("최종지불금액 :", price-discount)
    
else:
    print("물건가격 :", price)
    print("할인금액 :", discount)
    print("최종지불금액 :", price)