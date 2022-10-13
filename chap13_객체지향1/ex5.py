# 원을 클래스로 표시
# 반지름 r을 가지고 있다. 
# 원의 넓이와 원의 둘레를 계산하는 method를 정의
# 생성자는 매개변수가 있는 생성자를 사용하고, 출력결과는 예를들면
# 원의 반지름 : 10, 원의 넓이 : ..., 원의 둘레 : ...
# 원의넓이 : r^2*pi, 원의둘레 : 2*pi*r

from math import *


class Circle:
    radius = 0
    # 생성자
    def __init__(self, radius):
        self.radius = radius
    
    def circle_area(self):
        area = pow(self.radius,2) * pi
        return area
    
    def circle_circum(self):
        circumf = 2 * pi * self.radius
        return circumf
    
    
    
    
if __name__ == "__main__":
    circle1 = Circle(10)
    print("원의 반지름 : ", circle1.radius)
    # print("원의 넓이 : ", round(circle1.circle_area(),2))
    # print("원의 둘레 : ", round(circle1.circle_circum(),2))
    print("원의 넓이 : {:.2f}".format(circle1.circle_area()))
    print("원의 둘레 : {:.2f}".format(circle1.circle_circum()))