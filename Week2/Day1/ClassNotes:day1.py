

class Dog():
    def __init__(self, name, color):
        print("an object was created")
        self.name = name
        self.color = color
    def bark9(self):
        print(f'{self.name} barks WAf!')
    def walk(self,distanse:int):
        print(f'{self.name} walks {distanse}km')
    def rename(self,new_name):
        self.name=new_name
        return self.name
# ____________>

#dianas_dog = Dog()
#    dianas_dog.name='Leto'
 #   dianas_dog.color='Brown'

alex_dog=Dog('Rex',"beige")
john_dog=Dog('Fluffy',"white")

alex_dog.walk(5)
alex_dog.rename('Korn')
print(alex_dog.name)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



class BankAccount():
    def __init__(self, account_number,balance=o):
        self.account_number=account_number
        self.balance=balance
        self.transactions=[]
    def view_deposit(self,dep_amount):
        if dep_amount <=0:
            print("invalid amount")
        elif dep_amount<50:
            print('min deposit is 100')
        else:
            self.balance+=dep_amount
            self.view_deposit()
            self.transactions.append("deposit")


    def view_transactions(self):
        print('\n'.join(self.transactions))


    account1=BankAccount(1234567,500)
    account1.deposit(300)
    account1.viwe



