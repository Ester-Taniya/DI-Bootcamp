import random

from Exercise_XP import Dog

# 2
class PetDog(Dog):

    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        # 3
        self.trained = False

    # 4
    def train(self):
        super().bark()
        self.trained = True
        print(f'{self.name} now is trained!')

    def play(self, *args):
        dog_names = [dog.name for dog in args]
        print(f'{", ".join(dog_names)} all play together')

    def do_a_trick(self):

        trick1=f'{self.name} does a barrel roll'
        trick2=f'{self.name} stands on his back legs'
        trick3=f'{self.name} shakes your hand'
        trick4=f'{self.name}plays dead'
        tricks = [trick1,trick2,trick3,trick4]
        if self.trained == True:
            print(random.choice(tricks))
        else: print(f'{self.name} is not trained.')


dog4 = PetDog('Rassel', 8, 3.4)
dog5 = PetDog('Mojo', 1, 1.3)


#output

print(dog4.name)
PetDog.train(dog4)
PetDog.play(dog4, dog5)
PetDog.do_a_trick(dog4)
PetDog.do_a_trick(dog5)

