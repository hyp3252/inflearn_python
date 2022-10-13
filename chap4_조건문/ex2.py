# 사용자에게 명령을 받아서 터틀그래픽 제어.

# left입력시 왼쪽으로 회전, right를 입력하면 오른쪽으로 회전


import turtle

t = turtle.Pen()
# 반복문 무한 루프
while True:
    direction = input("왼쪽=left, 오른쪽=right, 종료=quit 입력 : ")
    if direction=="left":
        t.left(60)
        t.forward(50)
    if direction=='quit':
        break
    if direction=='right':
        t.right(60)
        t.forward(50)
        
        

turtle.exitonclick()