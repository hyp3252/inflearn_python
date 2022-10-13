# 클래스 안에 상수를 많이 사용
# 상수는 보통 공유 변수형태로(클래스 변수) 지정하여 사용한다.


class Character:
    # 상수값 정의
    WEAK = 0
    NORMAL = 10
    STRONG = 20
    VERY_STRONG = 30
    
    
    def __init__(self):
        self.__hp = Character.NORMAL
        
        
    def level_up(self):
        self.__hp = Character.STRONG
    
    def damage(self):
        self.__hp = Character.WEAK
    
    def get_hp(self):
        return self.__hp
    
    # __str__() 메소드는 문자열을 리턴하게 해주는것이 주 목적
    def __str__(self):
        return "HP : " + str(self.__hp)
    
if __name__ == "__main__":
    ch = Character()
    print(ch)
    ch.level_up()
    print(ch)
    print(ch.get_hp())