# 논리연산자

# and, or, not

# 대학을 졸업하려면 적어도 140학점을 이수하고 평점은 2.0이상은 되어야한다.

num = float(input("이수학점을 적어주세요 :"))
avg_num = float(input("학점평균을 적어주세요 :"))

if num >=140 and avg_num>= 2.0:
    print("대학졸업 대상자입니다.")
    
else:
    print("대학졸업이 불가합니다.")