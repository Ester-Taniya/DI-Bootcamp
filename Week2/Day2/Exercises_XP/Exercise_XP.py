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

cat1=Bengal('Salem',11)
cat2=Chartreux("Tom",2)
cat3=Siamese('Wiskers',5)

#2

all_cats = [cat1, cat2, cat3]
sara_pets = Pets(all_cats)

#4
sara_pets.walk()

#___________________________


#____Exercise 2 : Dogs _______________
class Dog():
    def __init__(self, name, age,weight):

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



dog1 = Dog('Rex', 2, 6.5)
dog2 = Dog('Jack', 7, 12.8)
dog3 = Dog('Moe', 12, 3.0)


print(dog1.name)
Dog.bark(dog3)
Dog.fight(dog1,dog2)


if __name__ == '__main__ '

#__________________________


'''_____________________________________________________________________________________________________________________________________'''

