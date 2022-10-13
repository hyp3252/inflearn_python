# 상위클래스 Shape 정의

from random import random, randrange
import turtle

class Shape:
    my_turtle = None
    cx, cy = 0, 0 # 도형의 중심점
    
    # 생성자
    def __init__(self):
        # Turtle 인스턴스 생성
        self.my_turtle = turtle.Turtle()
    
    def set_pen(self): # 펜 색상과 두께를 무작위로 선택
        r = random()
        g = random()
        b = random()
        print("r : {}, g : {}, b {}: ".format(r,g,b))
        
        self.my_turtle.pencolor((r,g,b)) # 펜 색상지정
        
        pen_size = randrange(1,20) # 펜의 굵기를 임의로 지정
        self.my_turtle.pensize(pen_size)
    
    # Shape 클래스를 상속받는 클래스들은 필요에 의해서 draw_shape()메소드를 오버라이딩을 할 수 있도록 선언부와 아무런 내용이없는 구현부
    def draw_shape(self):
        pass
    
    