# 구구단 출력프로그램

num = int(input("몇단 출력? : "))

for i in range(2, num+1):
    if num == i:
        for j in range(1, 10):
            print(i,"X",j,'=', i*j)