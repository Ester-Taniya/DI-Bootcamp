'''___Exercises XP_____________________________________________________________________________________________________________________________________'''

#____Exercise 1 – Random Sentence Generator   _____
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
def get_words_from_file():
    with open(dir_path + '/sowpods1.txt', 'r') as file:
        text = file.read().split('\n')
    print(text)
get_words_from_file()



























'''_____________________________________________________________________________________________________________________________________'''

