
from module import *

end_input = ""
print("이름과 나이를 입력해주세요. ((입력종료) : q)")

while True:
    if end_input == "n":
        print("입력을 종료합니다.")
        break
    
    else:
        name = input("회원명 입력 : ")
        age = int(input("회원님의 나이를 입력해주세요 : "))
        print_info(name, age)
    
    end_input = input("계속 입력하시겠습니까?(y / n) : ")