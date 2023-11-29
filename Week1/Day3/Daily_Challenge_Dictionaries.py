'''____________Daily Challenge: Dictionaries_____________________________________________________________'''

#_______Challenge 1 ______________
word = input("Enter a word: ")

letter_indexes = {}
for index, letter in enumerate(word):
    letter = str(letter)
    letter_indexes.setdefault(letter, [])
    letter_indexes[letter].append(index)

print(letter_indexes)

#_________________________________

