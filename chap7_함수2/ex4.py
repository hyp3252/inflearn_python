# 지역변수(local variable)와 전역변수(global variable)


def test():
    global text
    print(text)
    text = '파이썬 공부'
    print(text)
    


text = '자바공부'
test()
print(text)