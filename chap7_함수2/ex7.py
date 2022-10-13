# 원의 면적과 원의 둘레를 구하는 프로그램 작성
# PI = 3.141592 전역상수를 선언하고 상수를 활용

# 원의 면적 : r^2 pi, 원의 둘레 : 2 pi r


def main():
    r = float(input("원의 반지름을 입력 : "))
    area, circum = circle(r)

    print("반지름 {}인 원의 면적 : {}, 원의 둘레 : {}".format(r, area, circum))


PI = 3.141592
def circle(r):
    circle_area = pow(r,2) * PI
    circle_circum  = 2 * r * PI
    return circle_area, circle_circum

main()