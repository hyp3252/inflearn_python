# 계좌에 돈을 저금할 수 있고, 인출을 할 수도 있다.
# 클래스로 정의
# 은행계좌(Account)는 현재잔액(balance)를 field로 선언하고 기본생성자를 작성하고 입금(deposit), 출금(withdraw) 메소드를 작성

# 출력결과
# 통장에 1,000,000원이 입금됨.
# 현재잔액 : 1,000,000원
# 통장에 200,000원 출금
# 현재잔액 : 800,000원


class Account:
    balance = 0
    def __init__(self):
        self.balance = 0
        
    def deposit(self, amount):
        self.balance += amount
        print("통장에", format(amount, ","),"원이 입금됨.")
        print("현재잔액 :",format(self.balance, ","),"원")
        
    def withdraw(self, amount):
        self.balance -= amount
        print("통장에", format(amount, ","),"원이 출금됨.")
        print("현재잔액 :",format(self.balance, ","),"원")
        
        

if __name__ == "__main__":
    account1 = Account()
    account1.deposit(1000000)
    account1.withdraw(200000)