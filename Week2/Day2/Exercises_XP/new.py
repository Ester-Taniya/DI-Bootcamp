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

#1
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

cat1 = Bengal('Salem',11)
cat2 = Chartreux("Tom",2)
cat3 = Siamese('Wiskers',5)

#2

all_cats = [cat1, cat2, cat3]
sara_pets = Pets(all_cats)

#4
sara_pets.walk()

#___________________________


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

if __name__ == '__main__':

    dog1 = Dog('Rex', 2, 6.5)
    dog2 = Dog('Jack', 7, 12.8)
    dog3 = Dog('Moe', 12, 3.0)


    print(dog1.name)
    Dog.bark(dog3)
    Dog.fight(dog1, dog2)



#____Exercise 3 : Dogs Domesticated (in a neew file "XP_3.py")



#____Exercise 4 : Family
class Family():
    def __init__(self,last_name:str):
        self.last_name = last_name
        self.members=[
        {'name':'Michael','age':35,'gender':'Male','is_child':False},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False}]

    def born(self, **kwargs):
        self.members.append(dict(kwargs))
        print(f"Congratulations! {kwargs['name']} is born into the {self.last_name} family.")

    def is_18(self, first_name):
        for member in self.members:
            if member['name'] == first_name and member['age']>18:
                return True

            else:return False

if __name__ == '__main__':


    famili_1 = Family("Jonson")
    famili_1.born(name='Timmy',age=0,gender='Male',is_child=True)

    print(famili_1.is_18('Michael'))
    print(famili_1.is_18('Timmy'))

