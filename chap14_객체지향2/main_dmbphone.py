# Phone() 클래스와 Dmb_Phone()를 이용하여 메인코드
from DMB_phone import *

if __name__ == "__main__":
    # 하위클래스의 인스턴스 생성
    dmb = DmbPhone("파이썬폰", "빨간색", 10)
    
    print("모델 : ", dmb.model)
    print("색상 : ", dmb.color)
    print("채널 : ", dmb.channel)
    
    
    dmb.power_on()
    dmb.ringing()
    dmb.send_voice("여보세요")
    dmb.receive_voice("안녕하세요")
    dmb.send_voice("네 안녕하세요")
    dmb.hang_up()
    
    
    # 하위 클래스에서 만든 DMB 메소드 사용
    print("==========================")
    dmb.turn_on_dmb()
    dmb.change_channel(15)
    dmb.turn_off_dmb()