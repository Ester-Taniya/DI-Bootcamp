'''___Exercises XP 2_____________________________________________________________________________________________________________________________________'''

from Exercise_XP import Dog

class PetDog(Dog):

    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(super().bark())
        self.trained = True
        print(f'{self.name} now is trained!')


    def play(self, *args):
        dog_names = [dog.name for dog in args]
        print(f'{", ".join(dog_names)} all play together')

dog4 = PetDog('Rassel', 8, 3.4)
dog5 = PetDog('Mojo',1 , 1.3)

print(dog4.name)
PetDog.train(dog4)
PetDog.play(dog4, dog5)









          


