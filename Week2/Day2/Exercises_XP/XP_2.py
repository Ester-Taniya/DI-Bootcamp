'''___Exercises XP 2_____________________________________________________________________________________________________________________________________'''

from Exercise_XP import Dog

class PetDog(Dog):

    def __init__(self, trained = False):
        self.trained = trained

    def train(self):
        Dog.bark
        self.trained=True

    def play(self,*args):
        dog_names=[*args] 
        print(f'{dog_names} all play together')







          


