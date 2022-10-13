from Shape import *

class Rectangle(Shape):
    width = 0
    height = 0
    
    def __init__(self,cx,cy):
        Shape.__init__(self)
        # 도형의 원점 상위클래스에서 가져온다.
        self.cx = cx
        self.cy = cy
        
        # 사각형의 넓이와 폭을 임의의 수로 결정
        self.width = randrange(20,100)
        self.height = randrange(20,100)
        print("width :", self.width)
        print("height :", self.height)
        
    
    # 상위클래스에서 draw_shape() 메소드 오버라이딩
    def draw_shape(self):
        # 사각형 그리기
        sx1, sy1 = 0, 0 # 좌상단 좌표값
        sx2, sy2 = 0, 0 # 우하단 좌표값
        
        sx1 = self.cx - (self.width/2)
        sy1 = self.cy + (self.height/2)
        sx2 = self.cx + (self.width/2)
        sy2 = self.cy - (self.height/2)
        print("좌상단 x좌표 :{}, 좌상단 y좌표 :{}, 우하단 x좌표 :{}, 우하단 y좌표 :{}".format(sx1,sy1,sx2,sy2))
        
        # 펜의 색상과 두께 설정하기 위해 상위클래스 메소드를 호출
        self.set_pen()
        self.my_turtle.penup()
        self.my_turtle.goto(sx1,sy1) # 펜을 좌측상단으로 이동
        self.my_turtle.pendown()
        self.my_turtle.goto(sx1, sy2)
        self.my_turtle.goto(sx2, sy2)
        self.my_turtle.goto(sx2, sy1)
        self.my_turtle.goto(sx1, sy1)
        
        
        