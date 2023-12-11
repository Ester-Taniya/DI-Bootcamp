'''___Exercises XP_____________________________________________________________________________________________________________________________________'''

#____Exercise 1 – Random Sentence Generator   _____

import os
import random
#1-3

dir_path = os.path.dirname(os.path.realpath(__file__))
def get_words_from_file():
    with open(dir_path + '/sowpods1.txt', 'r') as file:
        words = file.read().split()
    return (words)

words = get_words_from_file()
#4
def get_random_sentence(length):

    global words
    random_words_list = []
    for i in range(length):
        random_words_list.append(random.choice(words))
    return random_words_list
 #5

def main():
    print("Hello, welcome to the random sentence generator program. ")
    user_input= int(input('please enter the length (from 2 until 20) of the random sentence you want generate: '))
    if 2 <= user_input <= 20:
        random_words = get_random_sentence(user_input)
        sentence = ' '.join(random_words).lower()
        print(f'{sentence}.')
    else: print('sorry, the number not in range (2,20)')
main()





#____ Exercise 2: Working With JSON_______
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)
#1
salary_key_level = data['company']['employee']['payable']['salary']
 
#2
data['company']['employee']['birth_date'] = '1990-01-01'

#3
with open('new_json','w') as json_fail:
    json.dump(data,json_fail,indent=2)






















'''_____________________________________________________________________________________________________________________________________'''

