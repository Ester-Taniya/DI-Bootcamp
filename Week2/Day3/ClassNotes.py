"""

class Family():
    def __init__(self,last_name:str,members):
    self.last_name=last_name
    self.members=members

    Class TheIncredibles(Family):
        def incredeble_persentation(self):
            super().famyly_presentation()

    data2={}


#__________Daly chalange________________

class Pagination():
    def __init__(self, items, pagesize) -> None:
        self.items = items
        self.pagesize = int(pagesize)
        self.current_page = 1

    def getVisibleItems(self):
        '''return a list of items '''
        end_index = self.pegesize*self.current_page
        start_index=end_index-self.pegesize

        self.current_page=self.items[start_index:end_index]
        return self.current_page

    def nextPage(self):
        self.current_page +=1
        return self.current_page
        pass

    def prevPage(self):
        pass

    def nextPage(self):
        pass

    def firstPage(self):
        pass

    def lastPage(self):
        pass

    def goToPage(pageNum):
        pass


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
print(alphabetList)

p = Pagination(alphabetList, 4)
print(p.getVisibleItems())
print(p.nextPage())
print(p.getVisibleItems())

"""

#_________exeptoons

"""
def divide(x,y):
    try:
        result=x/y

    except:
        raise TypeError ('one of the arg is not int')

    #except:
        raise ZeroDivisionError ('cant divide by zero')
    else:
        print(result)
        #
print(divide(5,0))
print('type error',divide('e',4))
print(divide(8,2))


# import Moduls


class Circle:
    color = "red"

    def __init__(self, diameter):
        self.diameter = diameter

    def grow(self, factor=2):
        self.diameter = self.diameter * factor

    def get_color(self):
       return Circle.color

    def change_color(self,color):
        return self.color

circle1 = Circle(2)
print(circle1.color)
circle1.change_color('blue')#????????????????
print(circle1.color)
print(Circle.color)
"""




class Myclass:
    def __int__(self,value)->None:
        #self.val=int
        self.val=self.filter_int(value)


    @staticmethod
    def filter_int(value):
        if value not isinstance (value, int):
            raise TypeError
        else:
            return value

a=Myclass(5)
print(b.value)
b=Myclass('100')
print(b.value)


