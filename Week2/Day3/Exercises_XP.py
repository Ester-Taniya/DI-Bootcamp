'''___Exercises XP_____________________________________________________________________________________________________________________________________'''

#____Exercise 1: Currencies_____
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return (f'{self.amount} {self.currency}s')

    def __int__(self):
        return (int(self.amount))

    def __repr__(self):
        return (f'{self.amount} {self.currency}s')

    def __add__(self, other):
        try: return self.amount + other
        except: TypeError ("Different currency")
        if self.currency == other.currency:
            return self.amount+other.amount
        else: return (f"Cannot add between Currency type {self.currency} and {other.currency}")

    def __iadd__(self, other):
        if type(self.amount)==type(other):
            self.amount += other
            return self
        elif self.currency==other.currency:
            self.amount += other.amount
            return self
        raise TypeError (f"Cannot add between Currency type {self.currency} and {other.currency}")


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)


print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 +5)
print(c1 + c2)
#print(c1+c3) # check

print(c1)
c1 += 5
print(c1)

c1 += c2
print(c1)

print(c1 + c3)

#___________________________


#____ Exercise 2: Import ____________________
from func import add_func as fn
 
print(fn(1,2))

#__________________________





#____Exercise 3: String Module___________________


import random
import string

def generate_random_string(length=5):
    letters = string.ascii_letters
    random_string=''.join(random.choice(letters) for _ in range(length))
    return random_string

result = generate_random_string()
print(result)


#__________________________



#____ Exercise 4 : Current Date ____________________

from datetime import datetime

def display_current_date():
    current_date = datetime.now()
    print(f"Current Date : {current_date}")


display_current_date()
#__________________________





#____Exercise 5 : Amount Of Time Left Until January 1st  ____________________
from datetime import datetime, timedelta

def time_until_january_1st():
    current_date = datetime.now()
    jan_1st=datetime(current_date.year+1,1,1)
    time_left = jan_1st - current_date
    days_left= time_left.days
    hours_left, remainder = divmod(time_left.seconds, 3600)
    minutes_left, seconds_left = divmod(remainder, 60)
    print(f" Until 1st of January is in {days_left} days and {hours_left:02}:{minutes_left:02}:{seconds_left:02} hours.")
time_until_january_1st()

#__________________________


#____Exercise 6 : Birthday And Minutes  ____________________
import datetime

def minutes_lived(birthdate):
    import datetime

    birthdate = datetime.datetime.strptime(birthdate, "%d-%m-%Y")
    current_date = datetime.datetime.now()
    time_lived = current_date - birthdate

    minutes_lived = time_lived.total_seconds() / 60

    print(f"You have lived {int(minutes_lived)} minutes.")

birthdate_input = input("Enter your birthdate (DD-MM-YYYY): ")
minutes_lived(birthdate_input)
#__________________________




#____Exercise 7 : Faker Module  ____________________
from faker import Faker
fake = Faker()
users = []

def add_user():
    user = {'name': fake.name(), 'address': fake.address(), 'language_code': fake.language_code()}
    users.append(user)

for i in range(5):
    add_user()
    for u in users:
        print(u)
#__________________________

'''_____________________________________________________________________________________________________________________________________'''

