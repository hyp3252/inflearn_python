# Disk 클래스를 만든다. 상위 클래스

class Disk(object):
    __capacity = 0
    __rpm = 0
    
    def __init__(self, capacity, rpm):
        self.__capacity = capacity
        self.__rpm = rpm
    
    def get_capacity(self):
        return self.__capacity
    
    def get_rpm(self):
        return self.__rpm
        
    def show_print(self):
        return "디스크의 용량은 " + str(self.__capacity)+"GB 이며" + \
            " RPM은" + str(self.__rpm) + "이다."
            
