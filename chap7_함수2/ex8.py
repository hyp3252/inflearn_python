
# 여러개의 값을 반환하는 함수 실습
# 타 프로그래밍언어에서는 함수가 항상 하나의 return값을 반환하거나 반환값이 없다.
# python에서는 tuple을 이용하여 여러개의 return값을 반환할 수 있다.


def tuple_return():
    return 1,"ㅎㅇ",5.0

a,b,c = tuple_return()
print(type(tuple_return())) # tuple의 형태
tuple_variable = tuple_return()
print(a,b,c) # tuple
print(tuple_variable)




li = list(tuple_variable)
li += [10]
li.append(100)
print(li)
print(type(li))