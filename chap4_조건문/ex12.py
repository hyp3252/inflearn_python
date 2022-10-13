# 학점을 세부적으로 나눈다. 중첩 if else문을 이용

# 1. 사용자로부터 점수를 입력받는다
# 2. 95이상 100이하면 A+
# 3. 90이상 94이하면 A0
# 4. 다른 B,C,D도 위와같이
# 5. 단, F는 그냥 출력

score = int(input("점수를 입력 :"))

if score >= 90:
    if score >= 95:
        print("A+")
    else:
        print("A0")
        
elif score < 90:
    if score > 80:
        print("B")
    elif score > 70:
        print("C")
    elif score > 60:
        print("D")
        
        
else:
    print("F")