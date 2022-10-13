# 1~100까지 누적값을 구하는데 2000 이상이 되면 for문을 빠져나오는 프로그램


sum = 0

for i in range(1,101):
    if sum >= 2000:
        print("마지막으로 더해진 i값", i)
        break
    sum += i
print(sum)

