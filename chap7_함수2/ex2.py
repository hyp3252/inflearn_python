# 문자열 전달에 대한 실습
# 문자열에 대한 내용도 숫자형의 객체와 동일하게 변경될 수 없는 immutable object형태라는 사실


def change(string):
    string += "공부합니다."
    print("change 함수 내의 string값 : ", string)
    print("change 함수 내의 string의 주소 :", id(string))


msg = "안녕하세요 저는 파이썬을 "
print("호출 전 msg 값 : " + msg)
print("호출 전 msg의 주소 :", id(msg))

change(msg)

print("호출 후 msg 값 : " + msg)
print("호출 후 msg의 주소 :", id(msg))



