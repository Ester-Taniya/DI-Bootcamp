'''___Exercises XP_____________________________________________________________________________________________________________________________________'''

#____ Exercise 1: Cats _____

#1
class Cats:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cats('Kitty', 3)
cat2 = Cats('Max', 5)
cat3 = Cats('Salem', 11)

print(f'There is 3 cats:{cat1.name},{cat2.name} and {cat3.name}')

#2
def Oldest_cat(*args):
    the_oldest_cat = max(args, key=lambda cat: cat.age)
    return the_oldest_cat
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

            print(f"{self.name} jumps {self.height*2} cm high!")

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





#____ Exercise 3 : Who’s The Song Producer?  _________
#1
class Song:
    def __init__(self, lyrics: list):

        self.lyrics = lyrics

    #2
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()



#__________________________



#____Exercise 4 : Afternoon At The Zoo  ________
#1
class Zoo:
    #2
    def __init__(self, zoo_name):

        self.name = zoo_name
        self.animals = []


    #3
    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    # 4
    def get_animals(self):
        for animal in self.animals:
            print(animal)
    #5
    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f'{animal_sold} haw been sold')
        else:
            print(f'sorry no {animal_sold} in the {self.name}')
    #6
    def sort_animals(self):
        sorted_animals={}
        for animal in sorted(self.animals):
            first_letter = animal[0].upper()
            if first_letter not in sorted_animals:
                sorted_animals[first_letter] = [animal]
            else:
                sorted_animals[first_letter].append(animal)
        return sorted_animals

    #7
    def get_groups(self):
        sorted_animals = self.sort_animals()
        for key, value in sorted_animals.items():
            if len(value) == 1:
                print(f"{key}: {value[0]}")
            else:
                print(f"{key}: {value}")

    #8

ramat_gan_safari = Zoo(zoo_name="Ramat Gan Safari")

ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Emu")
ramat_gan_safari.add_animal("Eel")


ramat_gan_safari.get_animals()

ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Giraffe")

sorted_animals = ramat_gan_safari.sort_animals()
print(sorted_animals)

ramat_gan_safari.get_groups()
#__________________________


