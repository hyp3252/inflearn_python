from math import pi



def say_hello(name):
    print("안녕하세요, ", name)
    
    
def say_hello_msg(name, msg):
    print("안녕하세요, ", name, msg)
    
    

# 입력한 첫번째 숫자 부터 끝 숫자까지의 누적 합
def get_sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum


# 정수를 사용자로부터 입력받아서 제곱한 값을 반환하는 함수 (ex2)

def squared(num):
    # num = pow(num,2)
    return pow(num,2)


# 두 개의 정수를 입력받아 두 수 중 더 큰 수를 찾아서 큰 수를 리턴하는 함수(ex3, min,max구현)

def min_max(num1, num2):
    temp = 0
    if num1 > num2:
        temp = num1
    elif num1 < num2:
        temp = num2
    elif num1 == num2:
        print("두 수가 같습니다.")
    else:
        print("숫자를 잘못 입력 하셨습니다.")
        
    return temp



# 두 수를 입력받아서 거듭제곱을 구하는 함수
def power(x ,y):
    result = 1
    for i in range(y):
        result *= x
        
    return result



# 화씨온도를 섭씨온도로 변환하여 반환하는 함수 만들기 c_to_f() (ex4.py)
# F = (9.0/5.0) * C + 32
# C = (5.0 * (f-32)) / 9.0
def f_to_c(f):
    c = (5.0*(f-32)) / 9.0
    return c


# 소수를 판별하는 함수. is_prime() 작성 (ex5.py)
# 소수이면 true 리턴, 아니면 False


def is_prime(num):
    for i in range(2,num):
        temp = True
        if num % i == 0:
            temp = False
        else:
            temp = True
        return temp
    
    
    
    
# 함수가 리턴값이 없는 경우에 대한 예제(ex6.py)
def print_info(name, age):
    print("==================")
    print("이름 : ", name)
    print("나이 : ", age)
    print("==================")
    return

# default 인수
# 함수의 매개변수가 기본 값을 가지게 하는 방법(ex7.py)
def hello(name, msg="반갑습니다."):
    print(name + msg)
    
    
# keyword 인수
# 함수의 매개변수의 위치를 기준으로 하여 매칭을 해줌으로써 함수에 값이 전달(ex7.py)
def calc(x,y,z):
    return x-y-z



# 구의 부피를 계산하는 함수 sphere_volume()를 작성.
# 반지름을 입력받아 구의 부피를 구하는 함수를 호출(ex8.py)
# V = 4 / (3*pi*r^3)

def sphere_volume(r):
    V = (4 * pi * pow(r, 3)) / 3
    return V


# 1회용 password 생성기를 이용하여 3개의 password를 생성하여 출력하는 프로그램 작성(ex9.py)
# password길이는 6개자리로 한정
import random

def make_pw():
    num_str = "0123456789"
    password = ""
    
    for i in range(6):
        index = random.randrange(len(num_str)) # 길이에 대한 내용
        password += num_str[index]
    return password


# 10진수를 2진수로 변환하는 함수 ten_to_bi() (ex9.py)
def dec_to_bi(num):
    binary = ""
    while num != 0:
        value = num % 2
        if value == 0:
            binary = "0" + binary
        else:
            binary = "1" + binary
        num = num // 2
        print("num : ", num)
        # print(binary)
    return binary