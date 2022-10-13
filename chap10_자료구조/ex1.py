# 자료구조 : 데이터의 특징을 고려하여 데이터를 저장하는 방법
# 자료구조의 특징 : 메모리를 최대한 효율적으로 저장 및 반환하는 방법으로, 데이터를 관리하는것

##################스택(Stack)##################

stack_data = []
stack_data.append(10)
stack_data.append(20)
stack_data.append(30)
stack_data.append(40)
stack_data.append(50)
stack_data.append(60)

print(stack_data)
print(stack_data.pop())
print(stack_data.pop())
print(stack_data.pop())
print(stack_data.pop())
print(stack_data.pop())
print(stack_data) # 데이터를 삭제하면서 데이터 반환

##################입력받은 텍스트를 역순으로 추출##################

word = input("문자열 입력: ")
# list 메소드를 사용하여 문자열을 리스트로 반환
word_list = list(word)
print(word_list)

result = []

for _ in range(len(word_list)): # _ 기호는 for문을 돌릴 때, 변수에 값을 사용하지 않을 때, 메모리 절약차원에서 _에 할당받는것이다.
    result.append(word_list.pop())
    
print(result)