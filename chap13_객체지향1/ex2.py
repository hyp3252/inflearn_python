from TV import *

if __name__ == "__main__":
    # 인스턴스 2개생성
    tv1 = TV()
    tv2 = TV()
    
    # 인스턴스와 필드와 메서드를 tv1 이라는 인스턴스명으로 조작
    tv1.color = "검정"
    tv1.on_off_power(True, "tv1")
    tv1.up_channel(9, "tv1")
    tv1.up_volume(25, "tv1")
    tv1.print_tv("tv1")
    tv1.on_off_power(False, "tv1")
    
    
    tv2.color = "흰색"
    tv2.on_off_power(True, "tv2")
    tv2.up_channel(17, "tv2")
    tv2.up_volume(50, "tv2")
    tv2.down_volume(25, "tv2")
    tv2.print_tv("tv2")
    tv2.on_off_power(False, "tv2")
    
    



