# 지역변수와 전역변수 2

def test(n1,n2):
    global a # 함수 내에서 전역변수 a를 사용하겠다
    a = 20 # 전역변수의 값을 변경
    n1 = n2
    n2 = n1
    b = 30 # 지역변수
    print(a,b,n1,n2)


a, b = 1, 5
n1,n2 = 77, 88
print(a,b,n1,n2)

test(n1,n2)

print(a,b,n1,n2)
