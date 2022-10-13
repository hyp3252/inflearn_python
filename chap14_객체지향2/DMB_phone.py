# Phone() 클래스의 하위클래스인 DmbPhone을 만듬

from Phone import *

class DmbPhone(Phone):
    # 멤버의 개수가 12개
    # 생성자
    def __init__(self, model, color, channel):
        # 상위클래스 호출하는 2가지 방법
        # super().__init__()
        Phone.__init__(self)
        self.model = model
        self.color = color
        self.channel = channel
        
    # 메소드 추가
    
    def turn_on_dmb(self):
        print("채널 : ", self.channel, "번 채널로 수신 시작")
        
    def turn_off_dmb(self):
        print("DMB 방송수신을 멈춤.")
        
    def change_channel(self, channel):
        self.channel = channel
        print("채널 : ", self.channel, "번으로 채널을 바꿉니다.")
        