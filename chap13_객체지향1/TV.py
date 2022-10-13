# TV를 설계하는 클래스

class TV:
    # 필드 선언
    color = "" # 티비색상
    power = False # 전원
    channel = 0 # 채널
    volume = 0 # 음량
    
    # TV의 전원을 켜거나 끄는 멤버메소드
    def on_off_power(self, power, tv):
        self.power = power
        if self.power == True:
            print("%s 전원이 켜졌습니다." % tv)
        else:
            print("%s 전원이 꺼졌습니다." % tv)
    
    # TV의 채널을 올리는 멤버메소드
    def up_channel(self, channel, tv):
        if channel < 0:
            print("channel은 음수값이 없습니다.")
            return
        if self.power == False:
            print("%s의 전원을 켜주세요" % tv)
            return
        self.channel += channel
    
    # TV의 채널을 내리는 멤버메소드
    def down_channel(self, channel, tv):
        if channel < 0:
            print("channel은 음수값이 없습니다.")
            return
        if self.power == False:
            print("%s의 전원을 켜주세요" % tv)
            return
        self.channel -= channel
            
    # TV의 volume을 올리는 멤버메소드
    def up_volume(self, volume, tv):
        if volume < 0:
            print("volume은 음수값이 없습니다.")
            return
        if self.power == False:
            print("%s의 전원을 켜주세요" % tv)
            return
        self.volume += volume
            
            
    # TV의 volume을 내리는 멤버메소드        
    def down_volume(self, volume, tv):
        if volume < 0:
            print("volume은 음수값이 없습니다.")
            return
        if self.power == False:
            print("%s의 전원을 켜주세요" % tv)
            return
        self.volume -= volume
            
            
    def print_tv(self, tv): # 인스턴스의 멤버변수들의 값을 찍어보는 용도로 사용
        print("%s의 색상 : %s" % (tv,self.color))
        print("%s의 channel : %d" % (tv,self.channel))
        print("%s의 volume : %d" % (tv,self.volume))
        