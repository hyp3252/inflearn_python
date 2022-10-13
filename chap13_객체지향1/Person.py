# 생성자의 개념
# 생성자는 인스턴스를 생성하면 무조건 호출되는 메소드

# 생성자의 기본
# __init__()이라는 이름을 갖고, 언더바가 2개붙은 것들은 파이썬에서 예약해 놓은것이므로 프로그램을 작성할 때는 이 이름을 사용하여 변수나 함수만들면 안된다.

## class A:
##      def __init__(self):
##          # 초기화할 코드 입력


# 생성자 실습
# 개념 : 인스턴스를 생성하기 위해 꼭 필요한 존재
# 필드 초기화 메소드 역할을 한다

class Person:
    name = ""
    age = 0
    height = 0
    weight = 0
    address = ""
    # 기본 생성자
    def __init__(self):
        self.name = "홍길동"
        self.age = 35
        self.height = 187
        self.weight = 80
        self.address = "충남"
        print("Person의 기본생성자 호출")
        
    # getter() 함수는 return값만 존재하고 매개변수는 존재하지않는다.
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_height(self):
        return self.height
    def get_weight(self):
        return self.weight
    def get_address(self):
        return self.address
    
    # setter() 메소드
    def set_name(self, name):
        self.name = name
        
    # __str__()메소드는 멤버변수의 값을 간단하게 확인하고자 할 때 사용하면 편리
    def __str__(self):
        print(self.name)
        print(self.age)
        print(self.height)
        print(self.weight)
        print(self.address)