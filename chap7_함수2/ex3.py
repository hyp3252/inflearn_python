# call by reference 에 대한 실습
# 함수를 호출할 때, 실질적인 주소값이 넘어가서 호출한 곳에 영향을 끼치는 형태
# 파이썬에서는 함수의 매개변수값이 전부 객체이기 때문에 list, dictionary 와 같은 mutable object는 변경가능하므로 call by objective-reference라고 한다.

# def change(lst):
#     print("change 함수 연산 전에 list 값 : ", lst)
#     print("change 함수 연산 전에 list 주소값 : ", id(lst))
#     lst += [100,200]
#     print("change 함수 연산 후에 list 값 : ", lst)
#     print("change 함수 연산 후에 list 주소값 : ", id(lst))
    
    
# list = ['ㅎㅇ', 1, 3, 2.2]

# print("change 함수 호출 전 list 값 : ", list)
# print("change 함수 호출 전 list 주소값 : ", id(list))

# change(list)

# print("change 함수 호출 후 list 값 : ", list)
# print("change 함수 호출 후 list 주소값 : ", id(list))




dic = {"name":"yong", "age":30, "height":187}
def change(dic):
    print("change 함수 연산 전에 dic 값 : ", dic)
    print("change 함수 연산 전에 dic 주소값 : ", id(dic))
    dic["몸무게"] = 80
    print("change 함수 연산 후에 dic 값 : ", dic)
    print("change 함수 연산 후에 dic 주소값 : ", id(dic))
    
    
print("change 함수 호출 전 dic 값 : ", dic)
print("change 함수 호출 전 dic 주소값 : ", id(dic))

change(dic)

print("change 함수 호출 후 dic 값 : ", dic)
print("change 함수 호출 후 dic 주소값 : ", id(dic))