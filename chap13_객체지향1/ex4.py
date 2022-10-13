# Monitor class를 이용한 실습
from Monitor import *

if __name__ == "__main__":
    # 매개변수가 있는 생성자를 호출하는 방법
    monitor1 = Monitor("SAMSUNG", 32, 290000, "검정")
    monitor1.__str__()
    
    
    monitor1.set_company("LG")
    monitor1.set_inch(40)
    monitor1.set_price(450000)
    monitor1.set_color("흰색")
    monitor1.__str__()