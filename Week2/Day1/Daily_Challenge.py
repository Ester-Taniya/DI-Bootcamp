'''___Daily Challenge_____________________________________________________________________________________________________________________________________''''
#1
class Farm:
    #2
    def __init__(self, name):

        self.name = name
        self.animals = {}
    #3 minimum 1 metodh


    #4
    def add_animal(self,animal,count=1):

        if animal not in self.animals:
            self.animals[animal]=count
        else: self.animals[animal] += 1


#5-6Bonus:
    def get_info(self):
        print(f"{self.name}s farm'\n")
        for key,value in self.animals.items():
            print(f'{key} : {value}\n')
        print('    E-I-E-I-0!')


#Expand The Farm #1
    def get_animal_types(self):
        return sorted(self.animals.keys())
#Expand The Farm #2

    def get_short_info(self):
        animal_types = self.get_animal_types()
        print(f"{self.name}’s farm has {', '.join(animal_types)}")




macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
(macdonald.get_info())

#Expand The Farm
print(macdonald.get_animal_types())
macdonald.get_short_info()


#__________________________

