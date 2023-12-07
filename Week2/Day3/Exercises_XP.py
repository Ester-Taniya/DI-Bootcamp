'''___Exercises XP_____________________________________________________________________________________________________________________________________''''

#____   _____
class Currency:
    def ___(self,lable,amount):
        self.lable =lable
        self.amount=amount

    def __str__(self):
        return f'{self.amount} {self.lable}'

    def __int__(self):
        return int(self.amount)
    def __add__(self, other):
        if self.lable== other.lable
            return  self.amount + other.amount
        elif type(other)==int:
            return int(self.amount)+other
        else:raise TypeError ('Different lables')


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
"""
'''
str(c1)
# '5 dollars'

int(c1)
# 5

>>> repr(c1)
# '5 dollars'

>>> c1 + 5
# 10

>>> c1 + c2
# 15

>>> c1 
# 5 dollars

>>> c1 += 5
>>> c1
# 10 dollars

>>> c1 += c2
>>> c1
# 20 dollars

>>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>

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

