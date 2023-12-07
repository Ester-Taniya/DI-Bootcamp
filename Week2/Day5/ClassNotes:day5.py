#Daily Challenge : Text Analysis
"""
import re
import os
import nltk


from collections import Counter

dir 


class Text:
    def __init__(self,text_str) -> None:
        self.text_str = text_str


    @classmethod
    def from_file(cls,text_file):
        with open(f'{dir __path__}')

    def frequency(self,word):
    list_words =  self.text_str.split()
    frequency=list_words.count(word)
    return f'The frequency of {word}is {frequency}'

    def most_common(self):
        self.text_str=self.text_str.lower()
        list_words=self.text_str.split()
        for i,word in enumerate(list_words):
           list_words[i]=re.sub() 
        c_obj = Counter(list_words)
        most_common=c_obj.most_common[0]
        word, times =most_common[0]
        return f"the most common words in the string are: {unique} "

    def unique_words(self):
        self.text_str=self.text_str.text_str.lower()

        for i,word in enumerate(list_words):
            list_words[i]=re.sub()
        unique= set(list_words) # because set hawe onli unique arguments
        return f"the unique words in the string are: {unique} "

"""
##### python3 -m pip install  requests
import requests

respponse= requests.get('https://api.chucknorris.io')
print(respponse)

print(respponse.json)


