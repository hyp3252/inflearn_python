# 1.증속, 2.감속, 3.중지 를 출력하고 사용자의 입력을 1,2,3으로 받아서
# 증속을 하면 속도를 10씩증가시키고, 감속을하면 10씩 감속을하고, 중지를 하면 무한루프를 빠져나간다.




run = True

speed = 0
keyCode = 0

while run:
    print("------------------------")
    print("1.증속 | 2.감속 | 3.중지 ")
    print("------------------------")
    keyCode = int(input("선택 : "))
    
    if keyCode == 1:
        speed += 10
        print("현재속도 : {}".format(speed))
    elif keyCode == 2:
        speed -= 10
        print("현재속도 : {}".format(speed))
    elif keyCode == 3:
        run = False
        print("중지하였습니다.")
    else:
        print("잘못된 입력값입니다.")
        
print("프로그램 종료")