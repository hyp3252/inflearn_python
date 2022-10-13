# 무명함수에 대한 실습
# lambda 인수1, 인수2 : x + y


# 일반적인 함수

def main():
    print('두 정수의 합 : ', get_sum(10,50))
    print('두 정수의 합 : ', get_sum(100,50))
    
def get_sum(x,y):
    return x+y

main()



# lambda 이용한 sum 함수

sum = lambda x,y : x+y
print("lambda식을 이용한 두 정수의 합", sum(10,50))
print("lambda식을 이용한 두 정수의 합", sum(100,50))