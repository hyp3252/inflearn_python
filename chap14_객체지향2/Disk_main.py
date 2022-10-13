# Disk, HDD의 실행 파일
from Hddisk import *

if __name__ == "__main__":
    disk = Disk(500, 7200)
    hddisk = Hddisk(32, 520)
    
    print(disk.show_print())
    print(hddisk.show_print())