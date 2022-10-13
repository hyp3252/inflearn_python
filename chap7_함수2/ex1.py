def change(num):
    num = num + 10
    print("change 함수 내의 num값 : ", num)
    print("change 함수 내의 num의 주소 :", id(num))

# 모든 값들은 객체
# id()함수는 매개변수 값으로 객체를 받아서 그 객체의 고유주소값을 반환
n = 100
print("호출 전 n의 주소 :", id(n))
print("호출 전 n값 : ", n)
change(n)
print("호출 후 n의 주소 :", id(n))
print("호출 후 n값 : ", n)



