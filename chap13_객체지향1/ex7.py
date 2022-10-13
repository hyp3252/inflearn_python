# 인스턴스 변수 : 인스턴스를 생성해야 비로소 사용
# 메모리 공간을 독립적으로 차지하고 있어서 해당 인스턴스에만 영향
# 인스턴스명.인스턴스변수명

## 클래스 변수 : 클래스가 로딩이 되며 클래스영역에 미리 공간을 할당하고 저장
## 클래스 변수는 모든 인스턴스에 공유되는 변수
## 클래스 변수의 접근방법은 : 클래스명.클래스변수명
## 클래스 변수의 값 변경은 모든 인스턴스에 영향을 미친다.



class Car:
    # color = ""
    # speed = 0
    count = 0 # 클래스 변수는 반드시 필드로 선언
        
    def __init__(self):
        self.color = '노란'
        self.speed = 0
        Car.count += 1 # 공유되는 클래스 변수
        
    def __str__(self):
        print("color : ", self.color)
        print("speed : ", self.speed)
        print("Car.count : ", Car.count)

if __name__ == "__main__":
    print(Car.count)
    print(id(Car.count))
    
    car1 = Car()
    car1.__str__()
    print(id(car1.count))
    
    car2 = Car()
    car2.__str__()
    print(id(car2.count))