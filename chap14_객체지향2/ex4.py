# None 참조값 : 변수가 아무것도 가르키고 있지 않다면 None으로 초기화를 해주는것이 권장사항
# 모든 변수는 초기화를 해주는것이 제일 좋다.
# None, Null 등은 아무것도 참조하고 있지 않다는 특별한 값


class TV:
    def __init__(self, power, channel, volume):
        self.power = power
        self.channel = channel
        self.volume = volume
        
    def power_tv(self):
        self.power = not self.power
    
    def __str__(self):
        print(self.power)
        print(self.channel)
        print(self.volume)
    
if __name__ == "__main__":
    tv1 = None # 초기화
    print(tv1) # 결과가 아무것도 가르키고 있지않으므로 None으로 나온다.
    # tv1.power()
    tv1 = TV(True, 10, 25)
    tv1.__str__()
    tv1.power_tv()
    print('=========================')
    tv1.__str__()