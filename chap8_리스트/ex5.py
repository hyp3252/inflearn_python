########################### 리스트 기초 연산실습 ###########################

# 리스트에 요소 삽입
# append() : 리스트 요소의 항상 마지막에 추가
# insert() : 리스트명.insert(인덱스, 추가할 요소), 원하는 인덱스위치에 요소를 추가가능



lst = [1,200,300]

lst.append("ㅎㅇ")
print(lst)

lst.insert(1, "ㅂㅇ")
print(lst)


# 리스트에서 요소 찾기
heros = ['토르', '헐크', '아이언맨', '스파이더맨']

print('토르' in heros)
print('슈퍼맨' not in heros)


idx = heros.index("헐크")
print("헐크의 인덱스 : ", idx)

if "ㅇㅇ" in heros:
    idx = heros.index("ㅇㅇ")
    print("ㅇㅇ 가 존재합니다.", idx)
else:
    print("ㅇㅇ 가 존재하지 않습니다.")
    
    
# 리스트에서 요소 삭제
# list.pop(index) : 리스트에서 인덱스에 해당하는 요소를 삭제하고 요소 반환
# list.remove(요소) : 리스트에서 요소를 삭제하고 반환을 하지않음
# del list[index] : 리스트에서 인덱스에 해당하는 요소 삭제 후 요소 반환을 하지않음

heros = ['토르', '헐크', '아이언맨', '스파이더맨']

element = heros.pop(-1)
print("element : ",element)
print(heros)

element = heros.remove("토르")
print("element : ",element)
print(heros)
