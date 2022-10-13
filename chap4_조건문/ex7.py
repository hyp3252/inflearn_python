# 문자열의 중앙에 있는 문자를 추출하여 출력하는 프로그램 만들기


# input : Monday, output : n,d
# input : weekday, output : k


string = input("문자열 입력 : ")
length = len(string)
print(string)
print(length)
if length % 2 == 1:
    print(string[length//2])
    
else:
    print(string[(length//2) - 1],string[length//2])
