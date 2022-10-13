# 함수를 사용한 프로그램 설계
# 1. 요구사항
# 2. 문제를 한 번에 해결하려고 하지말고 더 작은 단위까지 분리를 해주는게 좋다
# 3. 더 이상 분해가 되지 않는 부분에 도달했을 때 해당하는 기능을 함수로 만들어서 작성
# 4. 솔루션을 단위테스트 및 통합테스트까지 완료하고 배포 및 안정화

import grade

def main():
    score_list = grade.read_list()
    sorting_list = grade.sorting_list(score_list)
    grade.show_score(sorting_list)





if __name__ == "__main__": # 프로그램의 시작점
    main()