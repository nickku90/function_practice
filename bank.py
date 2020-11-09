class Banks():
    #定義銀行類別
    '''sfsdffsdfsdfs
    dsfsdfsdfdsfsd'''
    def __init__(self,uname,money):
        self.name=uname
        self.balance=money
        self.title="Taipei Bank"
    def save_money(self,money):
        self.balance+=money
        print("存款",money,"完成")
    def withdraw_money(self,money):
        self.balance-=money
        print("提款",money,"完成")
    def get_balance(self):
        print(self.title,"目前餘額:",self.balance)

hungbank=Banks("hung",100)
hungbank.get_balance()
hungbank.save_money(300)
hungbank.get_balance()
hungbank.withdraw_money(200)
hungbank.get_balance()

print(hungbank.__doc__)
