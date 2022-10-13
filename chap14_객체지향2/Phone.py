# Phone 클래스(상위클래스)
# 모든 클래스의 최상위 클래스는 object 클래스 ==> 적어주지않아도 된다.

class Phone(object):
    # 생성자
    # Phone()의 멤버의 개수는 8개.(object 멤버빼고)
    def __init__(self):
        self.model = ""
        self.color = ""
        
    # 메소드 정의
    def power_on(self):
        print("전원을 켭니다.")
        
    def power_off(self):
        print("전원을 끕니다.")
        
    def ringing(self):
        print("벨이 울립니다.")
        
    def send_voice(self, msg):
        print("자신 : " + msg)
        
    def receive_voice(self,msg):
        print("상대방 : " + msg)
    
    def hang_up(self):
        print("전화를 끊습니다.")