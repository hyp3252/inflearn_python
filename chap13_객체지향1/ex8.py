# 클래스 변수와 인스턴스 변수의 예


class Card:
    kind = '' # 무늬
    num = 0
    width = 100 # 클래스변수
    height = 200 # 클래스변수
    
    def __init__(self, kind, num):
        self.kind = kind
        self.num = num
        
    def __str__(self):
        print("무늬 : ", self.kind)
        print("숫자 : ", self.num)
        print("가로 : ", Card.width)
        print("세로 : ", Card.height)
        
        
if __name__ == "__main__":
    card1 = Card("다이아", 10)
    card1.__str__()
    print("-------------------")
    card2 = Card("스페이드", 11)
    card2.__str__()
    