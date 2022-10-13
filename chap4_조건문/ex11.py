# 사용자로부터 아이디를 입력받아 등록되어있는 아이디 인지를 검사
# 등록된 아이디는 리스트에 저장
# 아이디가 등록되어있다면 password를 물어본다, password = 1234 로 가정

ID = input("아이디를 입력하세요 :")
ID_list = ['a', 'b', 'c', 'd', 'e']
pw = str(1234)

if ID in ID_list:
    password = input("패스워드를 입력하세요 :")
    if password == pw:
        print("로그인 되었습니다.")
        
    else:
        print("비밀번호가 틀립니다.")
        
else:
    print("확인되지 않은 사용자입니다.")