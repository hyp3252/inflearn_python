# 몸무게와 키를 입력받고, BMI 수치가 20이상이고, 25미만이면 표준
# BMI 수치가 20미만이면 표준이하, BMI 수치가 25이상이면 표준 이상
# BMI = 몸무게 / (키*키)


weight = float(input("몸무게를 입력하세요 :"))
height = float(input("키를 입력하세요 :"))
height /= 100
BMI = weight / pow(height, 2)

if 20 <= BMI < 25:
    print("표준 BMI", BMI)
elif BMI < 20:
    print("표준 이하 BMI",BMI)
else:
    print("표준 이상 BMI",BMI)