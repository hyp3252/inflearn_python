# 사용자로부터 임의의 개수인 성적을 입력받아서 합계와 평균을 계산하고 출력

# 센티널은 음수의 값을 사용.


count = 0
sum = 0
score = 0
avg = 0

# 센티널을 사용자에게 제시하는 코드

print("종료하려면 음수값 입력 : ")

while score >= 0:
    score = int(input(str((count+1)) + ("번째 학생의 성적을 입력하세요 : ")))
    # 음수값인지 검사하는 코드
    if score >= 0:
        sum += score # 성적의 합계를 구하는 코드
        count += 1 # 학생의 수를 누적하는 코드
        
# 합계와 평균을 계산하고 출력
if count > 0:
    avg = sum / count
    
print(str(count+1) + "학생의 평균은 {} 입니다.".format(avg))