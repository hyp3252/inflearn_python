# i = 0

# while i < 5:
#     print("하위~")
#     i += 1
    
# print("반복종료")


# # 숫자 0~9까지 줄바꿈하지않고 출력

# i = 0
# while i < 10:
#     i += 1
#     print(i, end=" ")



# 정수 안의 각 자리수의 합을 구한다

# EX) 1234면 1+2+3+4

a = int(input("정수 입력 : "))
sum = 0
while a > 0:
    one = a % 10
    ten = (a % 100) // 10
    hun = (a % 1000) // 100
    thou = (a // 1000)
    sum = one + ten + hun + thou
    break
print(sum)