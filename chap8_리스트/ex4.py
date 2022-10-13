# 시퀀스 자료형 : 순서를 가지는 요소들로 구성된 자료형을 의미


words = "Nice to meet you"
print(words[0], words[4], words[-1])

list1 = ['apple', 'banana', 'peach', 'tomato']

print(list1[0], list1[-1])

# 시퀀스 길이
print(len(words))
print(len(list1))

# 시퀀스에서 가능한 연산과 함수
# 시퀀스 자료형은 플러스 연산이 가능하다.
li1 = [1,2]
print("li 1의 주소값 : ", id(li1))
li2 = [3,4,5]
print("li 2의 주소값 : ", id(li2))
li3 = li1+li2
print("li 3의 주소값 : ", id(li3))

# 시퀀스 자료형에서 * 연산자는 반복을 시킨다.
print(['ㅎㅇ', 'ㅂㅇㅂㅇ'] * 3)


# boolean 연산자
print(10 in [1,2,3]) # 리스트에 10이 있는지? ==> False
print(10 not in [1,2,3]) # 리스트에 10이 없는지? ==> True

# 두 방법은 동일한 출력을 갖는다.
lst = ['ㅎㅇ', 'yong', 10, 100 ,-1]
print(lst[-2])
print(lst[-2 + len(lst)])

