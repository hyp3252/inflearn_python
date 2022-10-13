# 학생들의 성적을 처리하는 프로그램을 만들기
# 조건 : 사용자로부터 성적을 입력을 받아 list에 저장 후
# 성적의 평균을구하고 해당 점수가 80점 이상인 학생의 수를 출력

# 출력결과
# 성적을 입력하세요 : 10
# 성적을 입력하세요 : 20
# 성적을 입력하세요 : 30
# 성적을 입력하세요 : 10
# 성적을 입력하세요 : 80
# 성적을 입력하세요 : 40
# 성적 평균은 31.67입니다.
# 80점 이상 성적을 받은 학생은 1명입니다.



# scores = []
# sum = 0
# mean = 0
# for i in range(6):
#     scores.append(int(input('성적을 입력하세요 : ')))
#     sum += scores[i]
# if scores >= 80:
    

# mean = sum/len(scores)
    
# print(scores)
# print(sum, mean)

STUDENT = 5
scores = []
sum_scores = 0
avg_scores = 0
cnt_80 = 0


for i in range(STUDENT):
    score = int(input("성적을 입력하세요 : "))
    scores.append(score) # 학생들의 성적을 List에 저장
    sum_scores += score
    if score >= 80:
        cnt_80 += 1

avg_scores = sum_scores / STUDENT

# 80점 이상 학생수 구하기

print("성적평균은 {} 입니다.".format(avg_scores))
print("80점 이상 성적을 받은 학생은 {} 명입니다.".format(cnt_80))