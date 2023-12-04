'''___Exercises XP_____________________________________________________________________________________________________________________________________''''

#____ Exercise 1: Cats _____

#1
class Cats:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
    def cats_list(selfself, cat_name, cat_age):
        #return list(cat_name, cat_age)
        print(list(cat_age,cat_name))


cat1 = Cats('Kitty', 3)
cat2 = Cats('Max', 5)
cat3 = Cats('Salem', 11)

#2
def Oldest_cat(*args):
    oldest_cat = max(args, key=lambda cat: cat.age)
    return oldest_cat
oldest_cat = Oldest_cat(cat1, cat2, cat3)

#3
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

#___________________________


#____ Exercise 2 : Dogs __________
#1
class Dog():
    def __init__(self, dog_name, dog_height):
        #2
        self.name = dog_name
        self.height = dog_height
    #3
    def bark(self):
            print(f"{self.name} goes woof!")

    #4
    def jump(self):
            print(f"{self.name} jumps {self.height} cm high!")

#5
davids_dog=Dog("Rex",50)

#6
print(davids_dog.name, davids_dog.height)
#for more ridable we can ptint sentence:
print(f"The name of David's dog is {davids_dog.name} ands his height is {davids_dog.height} ")
davids_dog.bark()
davids_dog.jump()

#7
sarahs_dog=Dog('Teacup',20)

#8
print(f"The name of Sarah's dog is {sarahs_dog.name} ands his height is {sarahs_dog.height} ")

#9
if davids_dog.height > sarahs_dog.height:
    print(f"The bigger dog is {davids_dog.name}")
elif sarahs_dog.height > davids_dog.height:
    print(f"The bigger dog is {sarahs_dog.name}")
else:
    print("Both dogs are of the same height.")

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

