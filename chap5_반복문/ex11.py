# 업다운 게임

from random import *


cnt = 0
num = randint(1,100)
print("발생한 난수의 값", num)


print("1~100사이의 값을 맞춰라")

while cnt < 10:
    guess = int(input("숫자를 입력하세요 : "))
    cnt += 1
    if guess == num:
        print("정답입니다. 시도횟수:{}".format(cnt))
        break
    elif guess < num:
        print("UP. {}번의 기회가 남았습니다.".format(10-cnt))
    elif guess > num:
        print("DOWN. {}번의 기회가 남았습니다.".format(10-cnt))
        

