from Rectangle import *

def screen_left_click(x,y):
    rect = Rectangle(x,y)
    rect.draw_shape()


if __name__ == "__main__":
    turtle.title("클래스를 이용한 사각형그리기")
    
    # 마우스 왼쪽버튼이 클릭이 되는것을 감지하는 리스너 메소드
    # 1은 왼쪽버튼, 2는 휠, 3은 오른쪽버튼
    turtle.onscreenclick(screen_left_click, 1)
    turtle.done() # turtle 그래픽 창을 닫히지 않게 하는 메소드