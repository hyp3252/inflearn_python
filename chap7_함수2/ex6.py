# 매개변수는 함수의 선언부에 존재하며 함수가 호출될 때 비로소 메모리에 할당이 된다.
# 매개변수 == 지역변수

def list_test(my_list):
    print("함수 내의 my_list 의 주소값 : ", id(my_list))
    my_list += [1,2,3,4] # 매개변수로 넘어온 my_list에 새로운 리스트를 할당
    print("함수 내의 my_list를 할당 후의 주소값 :", id(my_list))
    print("함수 내부에서의 my_list값 출력 : ", my_list)
    return


# my_list 타입은 list이므로 mutable object
my_list = [100,200,300,400]
print("함수 호출 전 my_list의 주소값 :", id(my_list))
list_test(my_list)
print("함수 호출 후 my_list의 주소값 :", id(my_list))
print("함수 외부에서의 my_list값 출력 : ", my_list)
