# 인스턴스가 함수에 인자값으로 전달될 때는 인스턴스 값을 변경가능

# 주소값이 전달이 되어 변경가능하다. call by value와 유사

# 사각형


from cv2 import rectangle


class Rectangle:
    
    def __init__(self, side=0): # 매개변수의 값이 주어지지 않을 때 0으로 초기화
        self.side = side
        
    # 정사각형의 면적을 출력하는 메소드
    def get_area(self):
        return pow(self.side, 2)
    
# 함수 정의
# 클래스 Rectangle 의 인스턴스와 횟수를 매개변수로 받아서 횟수 값이 0이 될 때까지 변의 길이와 면적을 출력해주는 함수
def print_area(rectangle, cnt):
    print("인스턴스의 주소(함수내의) :", id(rectangle))
    cnt = 10
    print("cnt의 주소(함수내의) :", id(cnt))
    
    print("변의 길이", "\t", "사각형 넓이")
    while cnt >= 1: # cnt가 1보다 클 때까지
        print(rectangle.side, "\t\t", rectangle.get_area())
        rectangle.side += 1
        cnt -= 1
        
        
        
if __name__ == "__main__":
    rectangle = Rectangle()
    print("인스턴스의 주소 :", id(rectangle))
    cnt = 5
    print("cnt의 주소(함수밖의) :", id(cnt))
    print_area(rectangle, cnt)
    print("정사각형 한 변의 길이 : ", rectangle.side)
    print("반복 횟수 : ", cnt)