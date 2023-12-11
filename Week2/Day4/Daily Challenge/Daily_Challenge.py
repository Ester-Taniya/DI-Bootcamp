'''___Daily Challenge_____________________________________________________________________________________________________________________________________'''
#____ Part I  _____

from collections import Counter
import os
import string


dir_path = os.path.dirname(os.path.realpath(__file__))


class Text():
    def __init__(self, text)-> None:
        self.text = text.lower().translate(str.maketrans('', '', string.punctuation))
        self.words_list = self.text.split()

    def word_frequency(self, word):

        frequency = self.words_list.count(word.lower())
        if frequency > 0:
            return (f'The frequency of word "{word}" is {frequency} ')

        else: return None


    def most_common_word(self):
        most_common = Counter(self.words_list).most_common()
        if most_common[0][1] == most_common[1][1]:
            return (f'The most common words are : "{most_common[0][0]}" and "{most_common[1][0]}"')

        else: return (f'The most common word is : "{most_common[0][0]}"')

    def unique_words(self):
        unique = set(self.words_list)
        return list(unique)

#____ Part II  _____

    @classmethod
    def from_file(cls, text_file_name):

        with open(dir_path + text_file_name, 'r') as file:
            text = file.read()
        return cls(text)



text=Text('A good book would sometimes cost as much as a good house.')
print(text.word_frequency('A'))
print(text.word_frequency('good'))
print(text.word_frequency('house'))
print(text.most_common_word())
print(text.unique_words())


text_from_file = Text.from_file('/the_stranger.txt')
print(text_from_file.word_frequency('A'))
print(text_from_file.word_frequency('good'))
print(text_from_file.word_frequency('house'))
print(text_from_file.most_common_word())
print(text_from_file.unique_words())






#___________________________


#___________________________
