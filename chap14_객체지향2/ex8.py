# super() 메소드 : 하위클래스에서 메소드 오버라이딩을 할 때, 상위클래스의 메소드나 필드를 사용해야 하는 경우가 있는데,
# 이 때 사용하는 것이 super() 메소드

class Car:
    value = "상위클래스 필드값"
    def car_method(self):
        print("상위클래스 메소드 호출")
    

class Sedan(Car):
    value = "하위클래스 필드값"
    def car_method(self):
        super().car_method()
        print("하위클래스 메소드 호출")
        print("상위클래스 value 값 :", super().value)
        print("하위클래스 value 값 :", self.value)
        
if __name__ == "__main__":
    sedan = Sedan()
    sedan.car_method()