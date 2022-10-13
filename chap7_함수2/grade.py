# grade 모듈

# 사용자로부터 성적을 입력받다가 사용자가 음수를 입력하면 입력받는것 종료
def read_list():
    score_list = [] # 성적을 저장할 리스트 타입 변수선언
    flag = True # 무한루프를 빠져나가기 위한 변수
    
    
    while flag:
        score = int(input("성적입력 ( 종료 시 음수입력) : "))
        # 음수가 들어왔는지 체크하는 부분(루프 탈출 구간)
        if score < 0:
            flag = False
        else:
            score_list.append(score)
    
    return score_list


# 성적을 오름차순으로 정렬하는 함수
def sorting_list(score_list):
    score_list.sort()
    return score_list


# sorting 된 성적 리스트를 출력하는 함수
def show_score(score_list):
    k = 0
    for i in score_list:
        print((k+1),"번째 성적", i)
        k += 1