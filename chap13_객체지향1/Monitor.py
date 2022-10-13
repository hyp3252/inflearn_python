class Monitor:
    # field 선언
    company = ""
    inch = 0
    price = 0
    color = ""
    
    
    # 파이썬에서는 2개 이상의 생성자를 만들 수 없다. 그래서
    # 오버로딩 : 같은 메소드명으로 다른일을 하게 만드는 작업
    # 매개변수의 타입과 개수에 따라서 같은 이름의 메소드라도 다른 메소드가 호출이 되는 형태를 지정
    # def __init__(self):
    #     print("기본생성자 호출")
    
    
    
    # 매개변수가 4개 존재하는 생성자
    def __init__(self, company, inch, price, color):
        # self. 은 멤버변수를 칭하는 것이며, 외부에서 생성자를 호출할 때 매개변수값으로 들어오는 것을 의미
        self.__company = company
        self.__inch = inch
        self.__price = price
        self.__color = color
        print("매개변수가 있는 생성자 호출")
        
    # getter() 를 만들어서 private 메소드에 접근
    # 값만 읽어가도록 해주는 메소드
    def get_company(self):
        return self.__company
    def get_inch(self):
        return self.__inch
    def get_price(self):
        return self.__price
    def get_color(self):
        return self.__color
    
    # setter() 메소드
    # 멤버변수값을 변경시켜주는 메소드
    def set_company(self, company):
        self.__company = company
    def set_inch(self, inch):
        self.__inch = inch
    def set_price(self, price):
        self.__price = price
    def set_color(self, color):
        self.__color = color
    
    
        
    
    # 멤버변수들의 값을 찍어보기 위한 메소드
    def __str__(self):
        print("제조사 : ", self.get_company())
        print("크기 : ", self.get_inch())
        print("가격 : ", self.get_price())
        print("색상 : ", self.get_color())