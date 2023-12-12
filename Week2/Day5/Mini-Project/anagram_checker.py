'''___Mini-Project : Anagram Checker_____________________________________________________________________________________________________________________________________'''

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

class AnagramChecker():
    def __init__(self,file_name) -> None:
        with open(dir_path + file_name, 'r') as file:
            self.words = file.read().split()
        return (self.words)


        

anagram_checker = AnagramChecker('/sowpods.txt')
print(anagram_checker.words)

'''_____________________________________________________________________________________________________________________________________'''

