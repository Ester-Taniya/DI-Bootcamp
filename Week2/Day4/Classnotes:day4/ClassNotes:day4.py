"""


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

'''
#________________________

#DAYLYCHALANGE________________________________________________________________________________________________________________________________________________
"""

import  math as m

class Circle:
    def __init__(self, radius, diameter) -> None:
        self.radius = radius
        self.diameter = diameter

    @classmethod
    def from_radius(cls, radius):
        return cls(radius=radius, diameter=radius*2)

    @classmethod
    def from_diameter(cls, diameter):
        return cls(radius=diameter/2, diameter=diameter)


    def circle_aria(self):
        aria= m.pi*(self.radius ** 2)
        return aria

    def __str__(self):
        return f' Circle diameter: {self.diameter}\n radius: {self.radius}'

    def __add__(self, other):
        return self.diameter + other.diameter

    def __gt__(self, other):
        return self.diameter > other.diameter

    def __eq__(self, other):
        return self.diameter == other.diameter

    def sort_circles(self, lts:list):
        lts.append(self)
        result=sorted(lts)# lamda
        return result


circle1=Circle.from_radius(30)
circle2=Circle.from_diameter(50)
circle3=Circle(10,20)

print(circle1.diameter)
print(circle2.diameter)#
#
print(circle1+circle2)#70
print(circle1>circle2)#True
print(circle1 == circle2)#False

#
print()
#for cicle in s_cicles:
 #   print(cicle.diameter)


"""



 #CLASSWORK_____________________
"""

 with open('example.txt',encoding='utf-8',made='r') as f:
    my_line="HELLO TESTING"
   # f.read()+=my_line
    original_text=f.read()
 
    #Warning in the fail


with open('example.txt', encoding='utf-8', mode='w+') as f:
    #f.write(my_line)# overwrite
    original_text = f.read()
    print(original_text)
    my_line = "\nHELLO TESTING"
    f.write(my_line)

   """


###### LECTURE EXAMPLE
"""
def read_file(file_name):
    with open('example.txt', encoding='utf-8', mode='w+') as f:
        file_txt = f.readlines()#get a list of the lines lines
        return file_txt

def read_and_write(file_name,txt_add):
    with open('example.txt', encoding='utf-8', mode='w+') as f:
        f.read()
        f.write(f'\n{txt_add}')
        #print(f.readlines())

read_and_write('example.txt','addinf from function')
print(read_file('example.txt'))

"""
##########
"""
def read_file(file_name):
    with open(file_name, encoding='utf-8', mode='r') as f:
        file_txt = f.read()#get a list of the lines lines
        return file_txt
    
print(read_file('nameslist.txt'))
print()
"""
#########
"""
Download this text file http://www.practicepython.org/assets/nameslist.txt and do the following steps

1 Read the file line by line
2 Read only the 5th line of the file
3 Read only the 5 first characters of the file
4 Read all the file and return it as a list of strings. Then split each word
5 Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
6 Append your first name at the end of the file
7 Append "SkyWalker" next to each first name "Luke"
"""

with open('nameslist.txt','r') as f:
    text=f.readlines()

print('step1 : ',text) #1 Read the file line by line

print('step2 : ',text[:5]) #2 Read only the 5th line of the file

print('step3 : ',text[5-1]) #Read only the 5th line of the file

for word in text:
    s=list(word)
    print(s)
cleaned_names=list(map(lambda s: s.strip('\n'),text))
print(cleaned_names)
darth=cleaned_names.count('Darth')
luke=cleaned_names.count('Luke')
lea=cleaned_names.count('Lea')
print(darth,luke,lea)

with open('nameslist.txt',mode='a') as f:
    f.write('n\Tatiana')

for i,name  in enumerate(cleaned_names):
    if name == 'Luke':
        cleaned_names[i]=f'Skywalker{name}'

print(cleaned_names)













