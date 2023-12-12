'''___Mini-Project : Anagram Checker_____________________________________________________________________________________________________________________________________'''

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

class AnagramChecker():
    def __init__(self,file_name) :
        with open(dir_path + file_name, 'r') as file:
            self.words = [word.lower() for word in file.read().split()]

    def is_valid_word(self, user_word):
        self.user_word = user_word.lower()
        #print(self.user_word)
        if self.user_word in self.words:
            #print(f'The word "{self.user_word}" is real!')
            return self.user_word
        else: #print(f'Sorry, the word "{self.user_word}" is not real.')
            return None

    def is_anagram(self,word):
        word = self.is_valid_word(word)
        if word ==None:
            print(f'Sorry, the word "{self.user_word}" is not real.')
        else:
            anagrams = [words for words in self.words if sorted(words) == sorted(word)]
            print(f'Heare is list  of anagrams to "{word}": {anagrams}')
        



    

sowpods_checker = AnagramChecker('/sowpods.txt')
#print(sowpods_checker.words)
sowpods_checker.is_valid_word('zymoid')
sowpods_checker.is_valid_word('zymoif')
sowpods_checker.is_valid_word('meat')
sowpods_checker.is_anagram('meit')
sowpods_checker.is_anagram('meat')

'''_____________________________________________________________________________________________________________________________________'''

