# 특수 메소드 : 인스턴스 간에 산술연산과 비교연산을 해주는 메소드
# EX) 인스턴스 a와 b 가 존재 할 때, a + b를 하게되면 주소+주소가 되는 형태이기 때문에 연산자체가 불가
# + 연산이 가능하게 하기위해 __add()__클래스 안에 메소드로 정의를 해주면 + 연산을 하게 되면 자동으로 __add()__를 호출 해준다.


# 연산실습

class Circle:
    def __init__(self, radius=0):
        self.radius = radius
    # 2개의 인스턴스를 매개변수로 받는다. (주소값 공유)    
    def __eq__(self, other): # 비교 연산을 가능하게 해준다.
        return self.radius == other.radius
    
    
if __name__ == '__main__':
    circle1 = Circle(10)
    circle2 = Circle(20)
    if circle1 == circle2:
        print("원의 반지름이 동일")
    else:
        print("원의 반지름이 다릅니다.")
    