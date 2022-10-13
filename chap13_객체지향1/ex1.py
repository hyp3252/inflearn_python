# 클래스

# 클래스요소 : 멤버변수(필드, 속성), 멤버메소드(기능), 생성자(필수)

### Car class

from turtle import color, speed


class Car:
    color = ""
    speed = 0
    # Car의 기능을 담당하는 멤버메소드
    def up_speed(self, speed): # 속도 높이는 메소드
        if speed < 0: # 음수를 입력방지하기 위한 조건문
            print("속도는 음수가 될 수 없습니다. ")   
            return
        self.speed += speed
    
    def down_speed(self, speed): # 속도 감소하는 메소드
        if speed < 0: # 음수를 입력방지하기 위한 조건문
            print("속도는 음수가 될 수 없습니다. ")   
            return
        self.speed -= speed
        
    # 멤버변수의 값을 출력해주는 메소드
    def print_fields(self, mycar):
        print("%s의 색상 : %s, 속도:%.2fKm" %(mycar, self.color, self.speed))

        
if __name__ == "__main__":
    # Car class의 인스턴스를 생성하여 사용하기
    my_car1 = Car()
    my_car2 = Car()
    my_car3 = Car()
    
    print("my Car1의 주소 : ", id(my_car1))
    print("my Car2의 주소 : ", id(my_car2))
    print("my Car3의 주소 : ", id(my_car3))
    
    print("-------------------------------")
    
    print("my Car1의 type : ", type(my_car1))
    print("my Car2의 type : ", type(my_car2))
    print("my Car3의 type : ", type(my_car3))
    
    my_car1.color = "파란색"
    my_car1.up_speed(50)
    my_car1.print_fields("my_car1")
    
    my_car2.color = "노란색"
    my_car2.up_speed(50)
    my_car2.down_speed(20)
    my_car2.print_fields("my_car2")
    
    my_car3.color = "빨간색"
    my_car3.up_speed(-100)
    my_car3.print_fields("my_car3")