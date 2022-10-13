# 메소드 오버라이딩 : 상속관계에서 상위클래스의 멤버메소드를 하위클래스에서 상속받아 자신의 기능에 맞게끔 "수정" 하는것.(modify, change)
# 단, 메소드의 선언부는 반드시 동일하고 구현부만 다르게.
# " 재정의 "

# 상위클래스 정의
class Car:
    speed = 0
    
    def up_speed(self, speed):
        self.speed += speed
        print("현재속도 (상위클래스) : %d" % self.speed)
        

# 하위클래스 정의
class Sedan(Car):
    # 메소드 오버라이딩
    def up_speed(self, speed):
        self.speed += speed
        # 150km/h 초과되지 못하게 Limit
        if self.speed > 150:
            self.speed = 150
            print("150km/h를 넘을 수 없습니다.")
        print("현재속도 (하위클래스) : %d" % self.speed)
        
# 하위클래스 정의
class Truck(Car):
    # 구현부에 Pass는 상위클래스의 멤버만 상속받고 자신의 멤버는 추가하지 않는다.
    pass
########################################################################################################################
########################################################################################################################


if __name__ == "__main__":

    sedan1 = Sedan()
    truck1 = Truck()
    print("승용차의 속도 : ", end=" ")
    # 메소드 오버라이딩이 되어진 하위클래스의 메소드가 호출
    sedan1.up_speed(200)
    
    print("트럭의 속도 : ", end=" ")
    truck1.up_speed(200)
    