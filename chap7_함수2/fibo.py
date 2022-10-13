# 피보나치 수열의 함수만 선언 및 구현 - 모듈의 형태

# 모듈 : 함수나 변수들을 모아 놓은 파일
# 자주 사용 될 것으로 예상되는 함수들을 선언 및 구현


def fib(n):
    n1 = 0
    n2 = 1
    n3 = n1 + n2
    while n3 < n:
        print(n3, end=" ")
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    print()
    
    
# 1~n까지의 합계를 구하는 함수
def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
        
    return sum

