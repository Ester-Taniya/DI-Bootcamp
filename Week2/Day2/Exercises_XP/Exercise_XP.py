'''___Exercises XP _____________________________________________________________________________________________________________________________________'''

#____Exercise 1 : Pets   _____
class Pets():
    def __init__(self, animals):
        self.animals = animals


    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#the input/output for ex of the end file  |||
#                                         VVV
#___because of the end file "if __name__ == '__main__':"  statment____________________________




#____Exercise 2 : Dogs _______________

class Dog():
    def __init__(self, name, age, weight):

        self.name = name
        self.age = age
        self.weight = weight


    def bark(self):
        print(f'{self.name} is barking')

    def run_speed(self):
        run_speed = self.weight / self.age*10
        return run_speed

    def fight(self,other_dog):
        self_run_speed = self.run_speed() * self.weight
        other_run_speed = other_dog.run_speed() * other_dog.weight
        if self_run_speed > other_run_speed:
            print(f'{self.name} won the fight!')
        elif self_run_speed < other_run_speed:
            print(f'{other_dog.name} won the fight!')
        else: print('It a draw!')

#the input/output for ex of the end file  |||
#                                         VVV
#__________________________________________________




#____Exercise 3 : Dogs Domesticated (in a neew file "XP_3.py")
#__________________________________________________


#____Exercise 4 : Family
class Family():
    def __init__(self,last_name:str, members:list):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(dict(kwargs))
        print(f"Congratulations! {kwargs['name']} is born into the {self.last_name} family.")

    def is_18(self, first_name):
        for member in self.members:
            if member['name'] == first_name and member['age']>18:
                return True
            else:return False

    def family_presentation(self):
        print(f'Family {self.last_name}:')
        for member in self.members:
            print(', '.join([f'{key}: {value}' for key, value in member.items()]))

#the input/output for ex of the end file  |||
#                                         VVV
#_________________________________________________





#____Exercise 5 : TheIncredibles Family
class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)

    def use_power(self, first_name):
        for member in self.members:
            if member['name'] == first_name:
                if self.is_18(first_name):
                    print(f'{first_name} can use power')
                else:
                    print(f"{first_name} can't use power because they are not 18 yet.")
                return

        print(f'No members with name {first_name} in {self.last_name} Family')

    def incredible_presentation(self):
        print(f"*Here is our powerful family*")
        super().family_presentation()

#the input/output for ex of the end file  |||
#                                         VVV
#_________________________________________________


if __name__ == '__main__':









#the input/output for EX1 (Cats)
    # 1
    cat1 = Bengal('Salem', 11) #1
    cat2 = Chartreux("Tom", 2)
    cat3 = Siamese('Wiskers', 5)

    # 2
    all_cats = [cat1, cat2, cat3]
    sara_pets = Pets(all_cats)

    # 4
    sara_pets.walk()
#______________________________________


# the input/output for EX1 (Dog)
    dog1 = Dog('Rex', 2, 6.5)
    dog2 = Dog('Jack', 7, 12.8)
    dog3 = Dog('Moe', 12, 3.0)

    print(dog1.name)
    Dog.bark(dog3)
    Dog.fight(dog1, dog2)
#______________________________________



#the input/output for ex4 (Family)
    family_1=Family('Jonson',[{'name':'Michael','age':35,'gender':'Male','is_child':False},{'name':'Sarah','age':32,'gender':'Female','is_child':False}])
    family_1.born(name='Timmy',age=0,gender='Male',is_child=True)
    print(family_1.is_18('Michael'))
    print(family_1.is_18('Timmy'))
    family_1.family_presentation()
# __________________________________________________



#the input/output for ex5 (Family)

    incredibles_family = TheIncredibles("Incredibles", [{'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},{'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}])

    incredibles_family.use_power('Ron')
    incredibles_family.use_power('Michael')
    incredibles_family.incredible_presentation()
    incredibles_family.born(name='Baby Jack', age=0, gender='Male', is_child= True, power='Unknown Power', incredible_name='Baby Jack')
    incredibles_family.incredible_presentation()


# __________________________________________________
