# 리스트에 대한 실습


scores = []
print("리스트 초기화 값 : ",scores)

# append로 int 값 추가
scores.append(30)
print("리스트 값 : ",scores)


# append로 str 값 추가
scores.append("ㅎㅇ")
print("리스트 값 : ",scores)

# append로 float 값 추가
scores.append(10.123)
print("리스트 값 : ",scores)
print("리스트 크기 : ", len(scores))


scores[0] = 'hello'
print("리스트 값 : ",scores)
print("리스트 크기 : ", len(scores))



# 리스트 순회해서 출력
for i in range(len(scores)):
    print(i, scores[i])
    
# 리스트 값을 순회해서 바꾸기
for i in range(len(scores)):
    scores[i] = i+10
    print(i, scores[i])
    
    
# 리스트 순회해서 출력 (for문과 리스트 시퀀스를 이용)
########################################## 에러남 ##########################################
# for i in scores: # 시퀀스를 사용하면 인덱스가 아닌 실제값을 가져와서 출력
#     scores[i] = i + 10
#     print(i, scores[i])


print("=======================================")


# # 사용자로부터 입력을 받아 리스트에 값을 저장
# nums = []
# for i in range(5):
#     nums.append(int(input("정수를 입력 : ")))
# print(nums)



# list 클래스, 기능 생성자
# 생성자를 이용한 리스트 만들기
li_1 = list() # 매개변수가 없는 생성자 호출
print("li_1 : ",li_1)
li_2 = list("안녕")
print("li_2 : ", li_2)

li_3 = list(range(0,5,2))
print("li_3 : ", li_3)

# 내장리스트 실습
li_1 = [12, 12.77, "ㅎㅇ"]
print("li_1 : ",li_1)
li_2 = [["서울", 10], ["뉴욕", 50], ["파리", 70]]
print("li_2 : ",li_2)
# 10을 출력하고싶으면
print("li_2 리스트에서 0번째 리스트 안에서의 1번째 인수 : ",li_2[0][1])

# list를 이중 for문으로 출력하기
# li_2[0][0], li_2[0][1], li_2[1][0], li_2[1][1], li_2[2][0], li_2[2][1] 값 들 출력
for i in range(len(li_2)):
    for j in range(len(li_2[i])): # li_2[0], li_2[1], li_2[2]
        print("####### li_2리스트의 각 행열 출력 : {}, {} #######\n\
####### li_2리스트의 각 행열값 출력 : {}".format(i, j, li_2[i][j]))