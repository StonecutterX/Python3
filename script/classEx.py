#/usr/bin/python3

"""
usage about class
"""
import json

class A(object):
    def __init__(self):
        print("test")
        
class Account(object):
    """
    user account,
    del_account(): delete account
    deposit():
    withdraw(): 
    inquiry(): check balance
    """
    num_accounts = 0
 
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Account.num_accounts += 1

    def del_account(self):
        Account.num_accounts -= 1

    def deposit(self, amt):
        self.balance = self.balance + amt

    def withdraw(self, amt):
        self.balance = self.balance - amt

    def inquiry(self):
        return self.balance

    def transfer(self, Account, amt):
        self.balance = self.balance - amt
        Account.balance = Account.balance + amt

    # 当name属性不存在时被调用
    def __getattr__(self, name):
        return "This attribute {} does not exist".format(name)

    # 类似于重载+操作符，
    # 包括其他item(如len, getitem，setitem, contains)都可以用__item__这种方式重载
    def __add__(self, account):
        return Account(self.name + " and " + account.name, self.balance + account.balance)
        
    @staticmethod
    def type():
        print("Current Account()")

    # 定义多个构造函数, 第一个参数为cls
    @classmethod
    def create(cls, name, balance):
        account = cls(name, balance)
        return account

    # 从json中读取，并初始化
    @classmethod
    def from_json(cls, param_json):
        params = json.loads(param_json)
        return cls(params.get("name"), params.get("balance"))

def AccountTest():
    #print(type(Account))
    #print(Account.num_accounts)
    #print(Account.deposit)

    x = Account('Jack', 1000)
    y = Account('Tom', 10000)
    print(x.inquiry())
    print(Account.num_accounts)

    x.deposit(111)
    print(x.inquiry())
    y.withdraw(999)
    print(Account.inquiry(y))

    print("deposit(): ",Account.deposit)
    print("type(): ", Account.type)

    mary = Account.create("Mary", 20000)
    print("Mary: ", mary.inquiry())

    #Account.transfer(mary, x, 2000)
    mary.transfer(x, 2000)
    print("Jack: ", x.inquiry())
    print("Mary: ", mary.inquiry())

    print(mary.number)
    print("mary + x = ", mary + x)

if __name__ == '__main__':
    AccountTest()
