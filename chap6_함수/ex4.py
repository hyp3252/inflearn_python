# 화씨온도를 섭씨온도로 변환하여 반환하는 함수 만들기 f_to_c() (ex4.py)

from module import *


temp_f = float(input("화씨온도 입력 : "))

print("화씨온도 : {0}, 섭씨온도 : {1:.2f}".format(temp_f, f_to_c(temp_f)))