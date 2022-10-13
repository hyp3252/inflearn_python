# 클래스의 상속 : 부모클래스, 슈퍼클래스의 멤버 (필드, 메소드)들을 그대로 자식클래스가 물려받아서 새로운 클래스를 만들어 준다.
# 상속이 이루어지면 직접적인 관계가 이루어진다.
# 상위클래스의 멤버가 추가, 삭제, 수정에 따라서 하위클래스가 영향을 받는다.
# 하위클래스의 멤버가 추가,삭제,수정되면 상위클래스에 영향을 미치지 않는다.
# 하위클래스로 내려가면 갈수록 멤버의 개수가 많아지고 상위클래스로 올라가면 멤버의 개수가 적어진다.


# 상위클래스
class Car:

    def __init__(self):
        self.speed = 0
        self.door = 0
    
    def up_speed(self, speed):
        self.speed += speed
        print("현재속도(부모클래스) : %d" % self.speed)
        print("문의 개수(부모클래스) : %d" % self.door)
        
        
# 하위클래스
class Sedan(Car):
    # 하위클래스의 멤버는 4개가 된다.
    def __init__(self, speed, door):
        Car.__init__(self) # 상위클래스의 생성자를 호출하는 부분.
        # super().__init__(speed, door)
        self.speed = speed
        self.door = door
        
    # 하위클래스에서 추가한 메소드
    def down_speed(self, speed):
        self.speed -= speed
        print("현재속도(자식클래스) : %d" % self.speed)


if __name__ == "__main__":
    
    car = Car()
    car.up_speed(50) # 상위클래스 메소드 호출
    print("car의 주소 : ", id(car))
    sedan = Sedan(100, 4)
    print("sedan의 주소 : ", id(sedan))
    sedan.up_speed(150) # 상위클래스 메소드 호출
    sedan.down_speed(100) # 하위클래스 메소드 호출