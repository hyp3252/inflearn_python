# from fibo import *
import fibo

# fibo.py module의 fib() 함수를 사용
# fibo.fib(100)
# print(fibo.sum(10))



# # __name__
# print(fibo.__name__)

# # 실행파일에서 __name__는 __main__ 값을 지니게 된다.
# print(__name__)

def main():
    fibo.fib(100)
    print(fibo.sum(10))
    print(fibo.__name__)
    print(__name__)
    

# 프로그램의 시작점이 되는 형태
if __name__ == "__main__":
    main()