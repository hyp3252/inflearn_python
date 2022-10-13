# 태어난 년도를 입력으로 받아서 초등,중,고등,대학 분류

# 8-13 초, 14-16 중, 17-19 고, 20-27 대

birth_year = int(input("태어난 년도를 입력: "))
present_year = int(input("현재 년도를 입력: "))

age = present_year - birth_year + 1

if 8 <= age <= 13:
    print("초등학생")
elif 14 <= age <= 16:
    print("중학생")
elif 17 <= age <= 19:
    print("고등학생")
elif 20 <= age <= 27:
    print("대학생")
else:
    print("일반인")