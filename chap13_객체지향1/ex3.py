from Person import *

if __name__ == "__main__":
    # 기본생성자 호출
    person1 = Person()
    person1.__str__()
    
    print("------------------------")
    
    person2 = Person()
    person2.__str__()
    
    
    
    print("------------------------")
    
    # 같은 필드의 값을 가지고 있지만 서로 다른 인스턴스
    print("person1의 주소 : ", id(person1))
    print("person2의 주소 : ", id(person2))