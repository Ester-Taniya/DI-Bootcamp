'''___Exercises XP_____________________________________________________________________________________________________________________________________''''

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


#____  ____________________
#__________________________





#____  ____________________
#__________________________



#____  ____________________
#__________________________




#____  ____________________
#__________________________


#____  ____________________
#__________________________




#____  ____________________
#__________________________

'''_____________________________________________________________________________________________________________________________________'''

