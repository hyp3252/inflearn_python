from Disk import *


class Hddisk(Disk):
    __capacty = 0
    __rpm = 0
    
    def __init__(self, capacity, rpm):
        Disk.__init__(self, capacity, rpm)
        self.__capacity = capacity
        self.__rpm = rpm
        
        
    def get_capacity(self):
        return self.__capacity
    
    def get_rpm(self):
        return self.__rpm
    
    def show_print(self):
        return "HD 디스크의 용량은 " + str(self.__capacity)+"GB 이며" + \
            " RPM은" + str(self.__rpm) + "이다."