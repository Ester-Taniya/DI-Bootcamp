'''___Mini-Project : Anagram Checker_____________________________________________________________________________________________________________________________________'''

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

class AnagramChecker():
    def __init__(self,file_name) :
        with open(dir_path + file_name, 'r') as file:
            self.words = [word.lower() for word in file.read().split()]

    def is_valid_word(self, user_word):
        self.user_word = user_word.lower()
        if self.user_word in self.words:
           return self.user_word
        else: return None

    def get_anagrams(self,word):
        word = self.is_valid_word(word)
        if word is None:
            print(f'Sorry, the word "{self.user_word}" is not real.')
        else:
            anagrams = [words for words in self.words if sorted(words) == sorted(word)]
            print(f'Heare is list  of anagrams to "{word}": {anagrams}')
        


if __name__ == "__main__":

 
    '''
    sowpods_checker = AnagramChecker('/sowpods.txt')
    print(sowpods_checker.words)
    sowpods_checker.is_valid_word('zymoid')
    sowpods_checker.is_valid_word('zymoif')
    sowpods_checker.is_valid_word('meat')
    sowpods_checker.get_anagrams('meit')
    sowpods_checker.get_anagrams('meat')
    '''

    

'''_____________________________________________________________________________________________________________________________________'''

