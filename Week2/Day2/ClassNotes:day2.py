
'''
class Animal():
    def __init__(self, mame, family, legs) -> None:
        self.name = name
        self.family = family
        self.legs = legs

    def make_sound(self):
        print(f" {self.name} is making a sound")

class Dog(Animal):
    pass

animal1= Animal('Bobo','ffe')

'''




'''     
#_____EX____________________________________________
class Dor():
    def __int__(self, is_opened):
        self.is_opened=is_opened

    def open_dor(self):
        self.is_opened=True
        print('The dor is open')

    def close_dor(self):
        self.is_opened = False
        print('The dor is close')


class BlockedDoor(Dor):
'''

# lecture_________________________
class AtmAccount:

    avalible_acc_num=2000

    def __init__(self, holder) -> None:
        self.__holder = holder
        self.__account_num = AtmAccount.avalible_acc_num
        self.__balance = 0
        AtmAccount.avalible_acc_num += 1

    @property # gives direc accese to priv
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,amount):
        self.__balance=amount



    def deposit(self,amount):
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        if amount > self.balance:
            raise ValueError
        else:self.balance-=amount

account1 = AtmAccount('Juliana S.')
account2 = AtmAccount('Tom S.')
account3 = AtmAccount('Leo Dicaprio.')
#print(account1.__holder)  #error
print(account1._AtmAccount__holder)
print(account1._AtmAccount__account_num)
print(account2._AtmAccount__account_num)
print(account3._AtmAccount__account_num)







