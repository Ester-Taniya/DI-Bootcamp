'''___Daily Challenge_____________________________________________________________________________________________________________________________________''''


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


#__________________________

