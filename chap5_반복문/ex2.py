# 사용자가 1부터 입력한 수 num까지 더해서 합계를 구하는 프로그램 for문을 통해 구하라

num = int(input("정수를 입력 :"))


sum = 0
for i in range(1, num+1):
    sum += i
print("1부터 {} 까지의 합계 : {}".format(num, sum))
