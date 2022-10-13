############################# 스택을 함수로 코딩 #############################


data = []
def push(data, n):
    data.append(n)
    return data

def pop(data):
    # 유효성 검사 (스택에 데이터가 없으면 에러를 발생시켜야 함)
    if len(data) > 0:
        return data.pop()
    else:
        print("스택이 비었습니다.")
        return
    
    
if __name__ == "__main__":
    stack = []
    for i in range(1, 5):
        push(stack, i)
        print("현재 스택 상태 : ", stack)
        
    for i in range(1, 5):
        pop(stack)
        print("현재 스택 상태 : ", stack)

print(push(data, 8))
print(pop(data))



